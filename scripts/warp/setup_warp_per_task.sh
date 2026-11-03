#!/usr/bin/env bash
# Prepare a server for WARP_PER_TASK (per-task, isolated WARP tunnels).
#
#   * installs wireproxy (userspace WireGuard -> local HTTP proxy) and wgcf,
#     pinned versions, SHA-256 verified;
#   * registers dedicated WARP account(s) for the bot into <bot>/CONFIG/warp/
#     (several tunnels can share one account; each tunnel still gets its own
#     egress IPv6 - more accounts only spread the load);
#   * --direct-route: if this server also runs a system-wide WARP (wg-quick@wgcf,
#     e.g. as the exit for a VPN), makes traffic generated locally by the bot's
#     user bypass it (ip rule uidrange ... lookup main) so Telegram never rides
#     the system tunnel; forwarded traffic (VPN clients, containers) is untouched.
#
# Usage (root):
#   scripts/warp/setup_warp_per_task.sh [--bot-dir DIR] [--accounts N] [--direct-route] [--uid UID]
set -euo pipefail

BOT_DIR=/root/Telegram/tg-ytdlp-bot
ACCOUNTS=1
DIRECT_ROUTE=0
BOT_UID=0
WIREPROXY_VER=1.1.3
WGCF_VER=2.3.1
declare -A WIREPROXY_SHA=(
    [arm64]=370e00bd2167960d1ecd1c3c1439715bbaa94a0a110a2040468670c9af6021b6
    [amd64]=e88c1d090740373fc606c1bafd81d9a5eadc642cce5667616e20e9d7a444f51c
)
declare -A WGCF_SHA=(
    [arm64]=710ab2d8ac145d81a4cf0c11bdb0e05914f77ae2a45f67b87e718d84b4cb7301
    [amd64]=4fb7a136aa470ece11d17949c7db07b040ec9c604742dc8680bcf1889f85d0c8
)

while [ $# -gt 0 ]; do
    case "$1" in
        --bot-dir) BOT_DIR="$2"; shift 2 ;;
        --accounts) ACCOUNTS="$2"; shift 2 ;;
        --direct-route) DIRECT_ROUTE=1; shift ;;
        --uid) BOT_UID="$2"; shift 2 ;;
        -h|--help) sed -n '2,19p' "$0"; exit 0 ;;
        *) echo "unknown option $1" >&2; exit 2 ;;
    esac
done
[ "$(id -u)" = 0 ] || { echo "run as root" >&2; exit 1; }
[ -d "$BOT_DIR" ] || { echo "no bot dir $BOT_DIR" >&2; exit 1; }
log() { echo "[setup-warp] $*"; }

case "$(uname -m)" in
    aarch64|arm64) ARCH=arm64 ;;
    x86_64|amd64) ARCH=amd64 ;;
    *) echo "unsupported arch $(uname -m)" >&2; exit 1 ;;
esac
TMP=$(mktemp -d)
trap 'rm -rf "$TMP"' EXIT

fetch() {  # url sha256 dest
    curl -fsSL -m 120 "$1" -o "$TMP/dl"
    echo "$2  $TMP/dl" | sha256sum -c --quiet - || { echo "checksum mismatch for $1" >&2; exit 1; }
    mv "$TMP/dl" "$3"
}

# ------------------------------------------------------------------ binaries
if ! /usr/local/bin/wireproxy --version 2>/dev/null | grep -q "$WIREPROXY_VER"; then
    log "installing wireproxy $WIREPROXY_VER ($ARCH)"
    fetch "https://github.com/windtf/wireproxy/releases/download/v$WIREPROXY_VER/wireproxy_linux_$ARCH.tar.gz" \
        "${WIREPROXY_SHA[$ARCH]}" "$TMP/wp.tgz"
    tar -xzf "$TMP/wp.tgz" -C "$TMP" wireproxy
    install -m 755 "$TMP/wireproxy" /usr/local/bin/wireproxy
fi
log "$(/usr/local/bin/wireproxy --version)"
WGCF=$(command -v wgcf || true)
[ -z "$WGCF" ] && [ -x /usr/local/bin/wgcf ] && WGCF=/usr/local/bin/wgcf
if [ -z "$WGCF" ]; then
    log "installing wgcf $WGCF_VER ($ARCH)"
    fetch "https://github.com/ViRb3/wgcf/releases/download/v$WGCF_VER/wgcf_${WGCF_VER}_linux_$ARCH" \
        "${WGCF_SHA[$ARCH]}" /usr/local/bin/wgcf
    chmod 755 /usr/local/bin/wgcf
    WGCF=/usr/local/bin/wgcf
fi

# ------------------------------------------------------------------ accounts
PROFILES="$BOT_DIR/CONFIG/warp"
install -d -m 700 "$PROFILES"
have=$(find "$PROFILES" -maxdepth 1 -name "*.conf" | wc -l)
n=$have
while [ "$n" -lt "$ACCOUNTS" ]; do
    n=$((n + 1))
    work="$TMP/acc$n"; mkdir -p "$work"
    for attempt in 1 2 3 4 5 6; do
        # Cloudflare answers 429 to quick successive registrations from one IP
        if (cd "$work" && "$WGCF" register --accept-tos >/dev/null 2>&1 && "$WGCF" generate >/dev/null 2>&1); then
            break
        fi
        [ "$attempt" = 6 ] && { echo "WARP registration failed (rate limited?); re-run later" >&2; exit 1; }
        log "registration rate-limited, waiting $((attempt * 60))s"
        sleep $((attempt * 60))
    done
    install -m 600 "$work/wgcf-profile.conf" "$PROFILES/account-$n.conf"
    install -m 600 "$work/wgcf-account.toml" "$PROFILES/account-$n.toml"
    log "registered WARP account $n -> $PROFILES/account-$n.conf"
    [ "$n" -lt "$ACCOUNTS" ] && sleep 150
done

# ------------------------------------------------------------------ direct route for the bot
# wg-quick sends everything "not fwmark <its mark>" into the WARP table and puts
# that rule ahead of all others again on every restart, so a uid ip-rule only
# lasts until the first rotation. Instead the bot's own packets get WARP's
# fwmark (iptables mangle OUTPUT, uid owner): they then use the main table
# whatever the rule order. Forwarded traffic (VPN clients, containers) never
# passes OUTPUT and keeps using WARP. Without native IPv6 the marked IPv6
# packets meet "no route" at once and the bot falls back to IPv4.
if [ "$DIRECT_ROUTE" = 1 ]; then
    MARK=$(ip rule show | sed -n 's/.*not from all fwmark \(0x[0-9a-f]*\) .*/\1/p' | head -1)
    MARK=${MARK:-0xca6c}
    HELPER=/usr/local/sbin/tg-ytdlp-direct-route
    cat > "$HELPER" <<EOF
#!/bin/sh
# tg-ytdlp-bot: packets of uid $BOT_UID carry the WARP fwmark $MARK and bypass wg-quick's table
MATCH="-m owner --uid-owner $BOT_UID -m comment --comment tg-ytdlp-direct -j MARK --set-mark $MARK"
case "\$1" in
start)
    for t in iptables ip6tables; do
        \$t -t mangle -C OUTPUT \$MATCH 2>/dev/null || \$t -t mangle -A OUTPUT \$MATCH
    done
    # rules of earlier versions (uid ip rules, lost on every wgcf restart)
    ip rule del priority 31000 2>/dev/null; ip -6 rule del priority 31000 2>/dev/null; ip -6 rule del priority 31001 2>/dev/null
    ;;
stop)
    for t in iptables ip6tables; do
        while \$t -t mangle -D OUTPUT \$MATCH 2>/dev/null; do :; done
    done
    ;;
esac
exit 0
EOF
    chmod 755 "$HELPER"
    UNIT=/etc/systemd/system/tg-ytdlp-direct-route.service
    cat > "$UNIT" <<EOF
[Unit]
Description=tg-ytdlp-bot: traffic of uid $BOT_UID bypasses the system-wide WARP (wgcf)
After=network-online.target
Wants=network-online.target
Before=tg-ytdlp-bot.service

[Service]
Type=oneshot
RemainAfterExit=yes
ExecStart=$HELPER start
ExecStop=$HELPER stop

[Install]
WantedBy=multi-user.target
EOF
    systemctl daemon-reload
    systemctl enable tg-ytdlp-direct-route.service
    systemctl restart tg-ytdlp-direct-route.service
    log "direct route active (fwmark $MARK): $(iptables -t mangle -S OUTPUT | grep tg-ytdlp-direct)"
fi

cat <<EOF

Ready. In $BOT_DIR/CONFIG/config.py:

  WARP_PER_TASK = True
  WARP_PROFILES_DIR = "CONFIG/warp"
  WARP_PROXY_HOST = "172.17.0.1"   # docker0 address if the bgutil PO-token container runs on Docker,
                                   # otherwise "127.0.0.1"

then restart the bot. Each task logs "[WARP] tunnel up ... egress=<IPv6>".
EOF
