@echo off
cls

set TOKEN="nhom7"
set REMOTE="bao-cao.herokuapp.com"
set LOCALPORT="8050"

cd ..
set /p INLETS_VERSION=<inlets_version

cd bin

if not exist inlets.exe (
  wget.exe https://github.com/inlets/inlets/releases/download/%INLETS_VERSION%/inlets.exe -O inlets.exe
)

inlets.exe client --remote="%REMOTE%" --token "%TOKEN%" --upstream=http://127.0.0.1:%LOCALPORT%
pause
