# VS Code Terminal Setup Script
# Run this in VS Code terminal to set up the environment

Write-Host "Setting up VS Code terminal for Django testing..." -ForegroundColor Green

# Navigate to the project directory
Set-Location "C:\Users\muzam\Desktop\CryptImage\Crypt-Image\CryptVault"

# Activate virtual environment
Write-Host "Activating virtual environment..." -ForegroundColor Yellow
& "..\env\Scripts\Activate.ps1"

# Verify Python path
Write-Host "Python path:" -ForegroundColor Cyan
where python

Write-Host "`nEnvironment ready! You can now run:" -ForegroundColor Green
Write-Host "  python manage.py test Vault" -ForegroundColor White
Write-Host "`nRunning tests now..." -ForegroundColor Yellow

# Run the tests
python manage.py test Vault
