#!/bin/sh
set -e

WG_DIR=/data
WG_CONF=/etc/wireguard/wgcf.conf

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

