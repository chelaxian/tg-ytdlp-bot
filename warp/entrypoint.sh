#!/bin/sh
set -e

WG_DIR=/data
WG_CONF=/etc/wireguard/wgcf.conf

# Install procps if sysctl is missing (fallback if Dockerfile wasn't updated)
if ! command -v sysctl >/dev/null 2>&1; then
  echo "[+] Installing procps (sysctl missing)"
  apt-get update -qq && apt-get install -y -qq procps >/dev/null 2>&1 || true
fi

mkdir -p /etc/wireguard "$WG_DIR"

if [ ! -f "$WG_DIR/wgcf-account.toml" ]; then
  echo "[+] Registering wgcf account"
  cd "$WG_DIR"
  wgcf register --accept-tos
fi

if [ ! -f "$WG_CONF" ]; then
  echo "[+] Generating WireGuard profile"
  cd "$WG_DIR"
  wgcf generate
  cp wgcf-profile.conf "$WG_CONF"
  chmod 600 "$WG_CONF"
fi

echo "[+] Starting WireGuard"
wg-quick up wgcf
echo "[+] WireGuard is up"
tail -f /dev/null
