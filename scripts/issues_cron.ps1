<#
.SYNOPSIS
    Sets up a Windows Scheduled Task to run /issues triage daily at 19:00 MSK.
.DESCRIPTION
    Creates a scheduled task that launches Kilo CLI in the project directory
    and executes the /issues command for automated daily issue triage.
    Run this script ONCE as Administrator (or current user) to register the task.
.NOTES
    Time: 19:00 Moscow (UTC+3) = 16:00 UTC. Windows Task Scheduler uses local time.
    Prerequisites: Kilo CLI must be installed and accessible in PATH.
#>

$ErrorActionPreference = "Stop"

$TaskName = "Kilo-Issues-Triage"
$ProjectPath = "L:\tg-ytdlp-NEW"
$NpxPath = (Get-Command npx -ErrorAction SilentlyContinue)?.Source

if (-not $NpxPath) {
    Write-Error "npx not found in PATH. Install Node.js first."
    exit 1
}

$existingTask = Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "Task '$TaskName' already exists. Removing to recreate..."
    Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
}

$Action = New-ScheduledTaskAction `
    -Execute $NpxPath `
    -Argument "kilo run --command /issues" `
    -WorkingDirectory $ProjectPath

$Trigger = New-ScheduledTaskTrigger -Daily -At "19:00"

$Settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1)

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $Action `
    -Trigger $Trigger `
    -Settings $Settings `
    -Description "Kilo: daily GitHub issue triage for tg-ytdlp-bot at 19:00 MSK" `
    -Force

Write-Host ""
Write-Host "Scheduled task '$TaskName' created successfully."
Write-Host "  Schedule: Daily at 19:00 (local time)"
Write-Host "  Working dir: $ProjectPath"
Write-Host "  Command: npx kilo run --command /issues"
Write-Host ""
Write-Host "To test manually: npx kilo run --command /issues"
Write-Host "To remove: Unregister-ScheduledTask -TaskName '$TaskName'"
