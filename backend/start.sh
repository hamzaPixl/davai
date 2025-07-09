#!/bin/bash

# DAVAI POC - Start Script
# Simple script to start the API server with uvicorn

echo "🚀 Starting DAVAI POC API Server"
echo ""

# Check if .env file exists
if [ ! -f .env ]; then
    echo "⚠️  Warning: .env file not found"
    echo "   Copy .env.example to .env and configure your API keys"
    echo ""
fi

# Get the Python executable path
PYTHON_PATH="/Users/hamzamounir/code/private/pixl/pocs/.venv/bin/python"
UVICORN_PATH="/Users/hamzamounir/code/private/pixl/pocs/.venv/bin/uvicorn"

# Check if virtual environment is active or use the venv path
if [ -z "$VIRTUAL_ENV" ]; then
    echo "💡 Using virtual environment at: /Users/hamzamounir/code/private/pixl/pocs/.venv"
    echo ""
fi

# Start the server
echo "🌐 Starting server..."
echo "📚 API Docs will be available at: http://localhost:8000/docs"
echo ""

# Run with uvicorn from venv
$UVICORN_PATH main:app --host 0.0.0.0 --port 8000 --reload --log-level info

echo ""
echo "👋 Server stopped"
