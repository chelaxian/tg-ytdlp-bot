@echo off
rem Stops only the two windows started by start_egress.cmd (matched by their exact window titles).
taskkill /F /FI "WINDOWTITLE eq egress-socks5*" /T >nul 2>&1
taskkill /F /FI "WINDOWTITLE eq egress-ssh*" /T >nul 2>&1
echo Stopped.
timeout /t 3 >nul
