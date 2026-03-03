#!/bin/bash
# Bot Resource Monitor Script
# Monitors file descriptors, threads, and network connections

BOT_NAME="tg-ytdlp-bot"
LOG_FILE="/var/log/bot-monitor.log"

# Function to log with timestamp
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

# Function to get bot process ID
get_bot_pid() {
    pgrep -f "python.*magic.py" | head -1
}

# Function to monitor resources
monitor_resources() {
    local pid=$(get_bot_pid)
    
    if [ -z "$pid" ]; then
        log "❌ Bot process not found!"
        return 1
    fi
    
    log "🔍 Monitoring bot PID: $pid"
    
    # File descriptors
    local fd_count=$(ls -1 /proc/$pid/fd 2>/dev/null | wc -l)
    log "📁 File descriptors: $fd_count"
    
    # Threads
    local thread_count=$(ls -1 /proc/$pid/task 2>/dev/null | wc -l)
    log "🧵 Threads: $thread_count"
    
    # Network connections
    local tcp_connections=$(lsof -p $pid -nP 2>/dev/null | grep -c TCP)
    local udp_connections=$(lsof -p $pid -nP 2>/dev/null | grep -c UDP)
    log "🌐 TCP connections: $tcp_connections, UDP connections: $udp_connections"
    
    # CLOSE-WAIT connections (problematic)
    local close_wait=$(ss -tuln | grep -c CLOSE-WAIT)
    if [ "$close_wait" -gt 0 ]; then
        log "⚠️  CLOSE-WAIT connections detected: $close_wait"
    fi
    
    # Memory usage
    local memory_kb=$(ps -p $pid -o rss= 2>/dev/null | tr -d ' ')
    local memory_mb=$((memory_kb / 1024))
    log "💾 Memory usage: ${memory_mb}MB"
    
    # CPU usage
    local cpu_percent=$(ps -p $pid -o %cpu= 2>/dev/null | tr -d ' ')
    log "⚡ CPU usage: ${cpu_percent}%"
    
    # Check for hanging animations (py-spy dump)
    if command -v py-spy >/dev/null 2>&1; then
        local animate_threads=$(py-spy dump -p $pid 2>/dev/null | grep -c "animate_hourglass")
        if [ "$animate_threads" -gt 5 ]; then
            log "🚨 WARNING: Too many animation threads detected: $animate_threads"
        fi
    fi
    
    echo "---"
}

# Function to check if bot is responsive
check_responsiveness() {
    local pid=$(get_bot_pid)
    
    if [ -z "$pid" ]; then
        log "❌ Bot process not found!"
        return 1
    fi
    
    # Check if process is in uninterruptible sleep (D state)
    local state=$(ps -p $pid -o stat= 2>/dev/null | cut -c1)
    if [ "$state" = "D" ]; then
        log "🚨 CRITICAL: Bot is in uninterruptible sleep (D state) - likely hanging!"
        return 1
    fi
    
    # Check if process is consuming CPU but not progressing
    local cpu_percent=$(ps -p $pid -o %cpu= 2>/dev/null | tr -d ' ')
    if (( $(echo "$cpu_percent > 90" | bc -l) )); then
        log "⚠️  High CPU usage detected: ${cpu_percent}%"
    fi
    
    return 0
}

# Function to generate report
generate_report() {
    local pid=$(get_bot_pid)
    
    if [ -z "$pid" ]; then
        log "❌ Cannot generate report - bot process not found!"
        return 1
    fi
    
    log "📊 Generating detailed report for PID: $pid"
    
    echo "=== BOT RESOURCE REPORT ===" > /tmp/bot-report.txt
    echo "Timestamp: $(date)" >> /tmp/bot-report.txt
    echo "PID: $pid" >> /tmp/bot-report.txt
    echo "" >> /tmp/bot-report.txt
    
    # Process info
    echo "=== PROCESS INFO ===" >> /tmp/bot-report.txt
    ps -p $pid -f >> /tmp/bot-report.txt
    echo "" >> /tmp/bot-report.txt
    
    # File descriptors
    echo "=== FILE DESCRIPTORS ===" >> /tmp/bot-report.txt
    ls -la /proc/$pid/fd/ >> /tmp/bot-report.txt
    echo "" >> /tmp/bot-report.txt
    
    # Network connections
    echo "=== NETWORK CONNECTIONS ===" >> /tmp/bot-report.txt
    lsof -p $pid -nP | grep -E 'TCP|UDP' >> /tmp/bot-report.txt
    echo "" >> /tmp/bot-report.txt
    
    # Threads
    echo "=== THREADS ===" >> /tmp/bot-report.txt
    ls -la /proc/$pid/task/ >> /tmp/bot-report.txt
    echo "" >> /tmp/bot-report.txt
    
    # Memory map
    echo "=== MEMORY MAP ===" >> /tmp/bot-report.txt
    cat /proc/$pid/maps | head -20 >> /tmp/bot-report.txt
    echo "... (truncated)" >> /tmp/bot-report.txt
    
    log "📄 Report saved to: /tmp/bot-report.txt"
}

# Main monitoring loop
main() {
    log "🚀 Starting bot resource monitor..."
    
    while true; do
        monitor_resources
        check_responsiveness
        
        # Generate detailed report every 10 minutes
        if [ $(($(date +%M) % 10)) -eq 0 ]; then
            generate_report
        fi
        
        sleep 60  # Check every minute
    done
}

# Handle script arguments
case "${1:-monitor}" in
    "monitor")
        main
        ;;
    "report")
        generate_report
        ;;
    "check")
        check_responsiveness
        ;;
    "help")
        echo "Usage: $0 [monitor|report|check|help]"
        echo "  monitor - Start continuous monitoring (default)"
        echo "  report  - Generate detailed report once"
        echo "  check   - Check responsiveness once"
        echo "  help    - Show this help"
        ;;
    *)
        echo "Unknown command: $1"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac
