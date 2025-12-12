# Скрипт для загрузки файлов warp на сервер
param(
    [Parameter(Mandatory=$true)]
    [string]$Server,
    
    [Parameter(Mandatory=$true)]
    [string]$RemotePath
)

$warpFiles = @(
    "warp\Dockerfile",
    "warp\entrypoint.sh"
)

Write-Host "Загрузка файлов warp на сервер $Server..." -ForegroundColor Green

foreach ($file in $warpFiles) {
    if (Test-Path $file) {
        Write-Host "Загрузка $file..." -ForegroundColor Yellow
        scp $file "${Server}:${RemotePath}/warp/"
    } else {
        Write-Host "Файл $file не найден!" -ForegroundColor Red
    }
}

Write-Host "Готово!" -ForegroundColor Green

