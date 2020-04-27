@echo off
if exist %windir%\SysWOW64 (
 copy .\geckodriver.exe %USERPROFILE%\AppData\Local\Temp
)else (
 copy .\geckodriver32.exe %USERPROFILE%\AppData\Local\Temp
)
pause


