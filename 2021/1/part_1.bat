@echo off
setlocal enabledelayedexpansion

set /a index = 0
set /a increases = 0
set /a last = 99999999

for /f "tokens=*" %%a in (input.txt) do (
    set /a index+=1
    
    if %%a gtr !last! (
        set /a increases+=1
    )

    set /a last = %%a
)

echo %increases%
