@echo off

echo Installing requirements...
pip install requests browser-cookie3 tkinter

echo.
echo Requirements installed successfully.
echo Running Python script...

python "%~dp0\RRs Grabber.py"

pause
