@echo off
echo Setting up environment for Django testing...
echo.

REM Navigate to the project directory
cd /d "C:\Users\muzam\Desktop\CryptImage\Crypt-Image\CryptVault"

REM Activate the virtual environment
call ..\env\Scripts\activate.bat

echo Virtual environment activated!
echo You can now run: python manage.py test Vault
echo.
echo Running tests now...
python manage.py test Vault

echo.
echo Setup complete! You can now use 'python manage.py test Vault' directly.
pause
