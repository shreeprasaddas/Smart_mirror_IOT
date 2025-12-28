#!/bin/bash
# Docker deployment script for MagicMirror Voice Assistant

echo "🐳 MagicMirror Voice Assistant - Docker Setup"
echo "=============================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed!"
    echo "Install Docker: https://docs.docker.com/engine/install/"
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed!"
    echo "Install Docker Compose: https://docs.docker.com/compose/install/"
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Create .env file if it doesn't exist
if [ ! -f .env ]; then
    echo ""
    echo "📝 Creating .env file..."
    read -p "Enter your Groq API key: " api_key
    echo "GROQ_API_KEY=$api_key" > .env
    echo "DISPLAY=:0" >> .env
    echo "✅ .env file created"
fi

# Build Docker image
echo ""
echo "🔨 Building Docker image..."
docker-compose build

if [ $? -eq 0 ]; then
    echo "✅ Docker image built successfully!"
else
    echo "❌ Failed to build Docker image"
    exit 1
fi

# Start containers
echo ""
echo "🚀 Starting containers..."
docker-compose up -d

if [ $? -eq 0 ]; then
    echo "✅ Containers started successfully!"
    echo ""
    echo "📊 Container Status:"
    docker-compose ps
    echo ""
    echo "🌐 Access MagicMirror at: http://localhost:8080"
    echo "📹 Face Recognition API: http://localhost:5000"
    echo ""
    echo "📝 Useful commands:"
    echo "  View logs:    docker-compose logs -f"
    echo "  Stop:         docker-compose stop"
    echo "  Restart:      docker-compose restart"
    echo "  Remove:       docker-compose down"
else
    echo "❌ Failed to start containers"
    exit 1
fi
