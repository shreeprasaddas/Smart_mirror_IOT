@echo off
REM Docker deployment script for Windows
echo ================================
echo MagicMirror Voice Assistant
echo Docker Deployment for Windows
echo ================================
echo.

REM Check if Docker is installed
docker --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not installed!
    echo.
    echo Install Docker Desktop for Windows:
    echo https://docs.docker.com/desktop/install/windows-install/
    echo.
    pause
    exit /b 1
)

echo [OK] Docker is installed
echo.

REM Check if Docker is running
docker ps >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running!
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo [OK] Docker is running
echo.

REM Create .env file if it doesn't exist
if not exist .env (
    echo Creating .env file...
    set /p api_key="Enter your Groq API key: "
    echo GROQ_API_KEY=!api_key!> .env
    echo DISPLAY=:0>> .env
    echo [OK] .env file created
    echo.
)

REM Build Docker image
echo Building Docker image...
docker-compose build
if errorlevel 1 (
    echo [ERROR] Failed to build Docker image
    pause
    exit /b 1
)

echo [OK] Docker image built successfully!
echo.

REM Start containers
echo Starting containers...
docker-compose up -d
if errorlevel 1 (
    echo [ERROR] Failed to start containers
    pause
    exit /b 1
)

echo [OK] Containers started successfully!
echo.

REM Show status
echo Container Status:
docker-compose ps
echo.

echo ================================
echo Deployment Complete!
echo ================================
echo.
echo Access MagicMirror at: http://localhost:8080
echo Face Recognition API: http://localhost:5000
echo.
echo Useful commands:
echo   View logs:    docker-compose logs -f
echo   Stop:         docker-compose stop
echo   Restart:      docker-compose restart
echo   Remove:       docker-compose down
echo.
pause
