@echo off
echo Activating virtual environment and running Django tests...
echo.

REM Activate the virtual environment
call ..\env\Scripts\activate.bat

REM Run the tests
echo Running: python manage.py test Vault
python manage.py test Vault

echo.
echo Tests completed!
pause
