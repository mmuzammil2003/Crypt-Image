# PowerShell script to activate virtual environment and run tests
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force

# Navigate to the project directory
Set-Location "C:\Users\muzam\Desktop\CryptImage\Crypt-Image\CryptVault"

# Activate the virtual environment
& "..\env\Scripts\Activate.ps1"

# Run the tests
python manage.py test Vault

# Keep the window open
Read-Host "Press Enter to exit"
