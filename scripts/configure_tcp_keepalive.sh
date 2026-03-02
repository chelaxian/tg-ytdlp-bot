#!/bin/bash
# TCP Keepalive Configuration Script
# Prevents hanging connections and CLOSE-WAIT states

echo "🔧 Configuring TCP keepalive settings..."

# Create sysctl configuration file
cat > /etc/sysctl.d/99-tg-bot-keepalive.conf << 'EOF'
# TCP Keepalive settings for tg-ytdlp-bot
# Prevents hanging connections and CLOSE-WAIT states

# Time before sending keepalive probes (60 seconds)
net.ipv4.tcp_keepalive_time=60

# Interval between keepalive probes (15 seconds)
net.ipv4.tcp_keepalive_intvl=15

# Number of failed probes before connection is considered dead (4)
net.ipv4.tcp_keepalive_probes=4

# Enable TCP keepalive
net.ipv4.tcp_keepalive=1

# Additional TCP optimizations
net.ipv4.tcp_fin_timeout=30
net.ipv4.tcp_tw_reuse=1
net.ipv4.tcp_tw_recycle=0
EOF

# Apply the settings
echo "📝 Applying TCP keepalive settings..."
sysctl --system

# Verify the settings
echo "✅ Current TCP keepalive settings:"
echo "tcp_keepalive_time: $(sysctl -n net.ipv4.tcp_keepalive_time)"
echo "tcp_keepalive_intvl: $(sysctl -n net.ipv4.tcp_keepalive_intvl)"
echo "tcp_keepalive_probes: $(sysctl -n net.ipv4.tcp_keepalive_probes)"
echo "tcp_keepalive: $(sysctl -n net.ipv4.tcp_keepalive)"

echo ""
echo "🎯 Configuration complete!"
echo "These settings will help prevent hanging HTTP connections."
echo "Restart your bot service to ensure all changes take effect:"
echo "sudo systemctl restart tg-ytdlp-bot"
