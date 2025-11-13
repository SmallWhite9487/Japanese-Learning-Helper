@echo off
cd /d "%~dp0"
set /p msg="Please enter update info :"：
git add .
git commit -m "%msg%"
git push
pause
