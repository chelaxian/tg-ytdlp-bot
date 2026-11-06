@echo off
rem Lets the dashboard browser on the DE server leave to the internet through THIS PC (this PC's IP).
rem 1) a local SOCKS5 proxy on 127.0.0.1:1081 (refuses LAN / loopback targets)
rem 2) a reverse SSH tunnel: DE container 127.0.0.1:1081 -> this proxy
rem Leave both windows open while you log in to services in the panel. Then run stop_egress.cmd.
cd /d "%~dp0"
start "egress-socks5" /min cmd /c python socks5_server.py 1081
start "egress-ssh" /min cmd /c ssh -N -o ExitOnForwardFailure=no -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -R 127.0.0.1:1081:127.0.0.1:1081 de-dash
echo Started. In the panel (Browser tab) switch on "Leave through my PC", then restart the browser.
timeout /t 5 >nul
