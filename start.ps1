# Audio Manager Quick Start Script

Write-Host "🎵 Audio Manager - Quick Start Setup" -ForegroundColor Cyan
Write-Host "====================================`n" -ForegroundColor Cyan

# Check if Python is installed
Write-Host "Checking Python installation..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version
    Write-Host "✓ $pythonVersion found" -ForegroundColor Green
} catch {
    Write-Host "✗ Python is not installed. Please install Python 3.8 or higher." -ForegroundColor Red
    exit 1
}

# Create virtual environment
Write-Host "`nCreating virtual environment..." -ForegroundColor Yellow
if (Test-Path "venv") {
    Write-Host "✓ Virtual environment already exists" -ForegroundColor Green
} else {
    python -m venv venv
    Write-Host "✓ Virtual environment created" -ForegroundColor Green
}

# Activate virtual environment
Write-Host "`nActivating virtual environment..." -ForegroundColor Yellow
& ".\venv\Scripts\Activate.ps1"
Write-Host "✓ Virtual environment activated" -ForegroundColor Green

# Install dependencies
Write-Host "`nInstalling dependencies..." -ForegroundColor Yellow
pip install -r requirements.txt
Write-Host "✓ Dependencies installed" -ForegroundColor Green

# Run migrations
Write-Host "`nRunning database migrations..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate
Write-Host "✓ Database migrations completed" -ForegroundColor Green

# Create superuser prompt
Write-Host "`n" -ForegroundColor Yellow
$createSuperuser = Read-Host "Do you want to create a superuser for admin access? (y/n)"
if ($createSuperuser -eq 'y' -or $createSuperuser -eq 'Y') {
    python manage.py createsuperuser
}

# Start server
Write-Host "`n🚀 Starting development server..." -ForegroundColor Cyan
Write-Host "====================================`n" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:8000/" -ForegroundColor Green
Write-Host "Admin Panel: http://localhost:8000/admin/" -ForegroundColor Green
Write-Host "API Root: http://localhost:8000/api/`n" -ForegroundColor Green
Write-Host "Press Ctrl+C to stop the server`n" -ForegroundColor Yellow

python manage.py runserver
