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

# Wait for WireGuard to fully initialize
sleep 3

# Check DNS configuration 
echo "[+] Checking DNS configuration..."
if [ -f /etc/resolv.conf ]; then
  echo "[+] Current /etc/resolv.conf:"
  cat /etc/resolv.conf
fi

# Test DNS resolution using different methods
echo "[+] Testing DNS resolution..."
DNS_WORKING=false

# Try getent (most reliable in containers)
if command -v getent >/dev/null 2>&1; then
  if getent hosts google.com >/dev/null 2>&1; then
    echo "[+] DNS is working (getent test passed)"
    DNS_WORKING=true
  fi
fi

# If getent failed, try with explicit DNS servers
if [ "$DNS_WORKING" = "false" ]; then
  echo "[!] DNS resolution failed with default settings"
  echo "[!] This may cause issues - domain names may not resolve"
  echo "[!] IP addresses should still work"
  echo "[!] Note: In Docker with network_mode: service:warp, DNS is shared"
  echo "[!] The bot container should inherit DNS from this container"
fi

tail -f /dev/null
