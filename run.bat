@ECHO off
CHCP 65001 > NUL
set PYTHONIOENCODING=utf-8

python --version > NUL 2>&1
IF %ERRORLEVEL% NEQ 0 GOTO nopython

CMD /k python discordfm.py
GOTO end

:nopython
ECHO ERROR: Python has either not been installed or not added to your PATH.

:end
PAUSE
