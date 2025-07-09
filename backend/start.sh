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

# Check if virtual environment is active
if [ -z "$VIRTUAL_ENV" ]; then
    echo "💡 Tip: Consider activating a virtual environment first"
    echo "   python -m venv venv && source venv/bin/activate"
    echo ""
fi

# Start the server
echo "🌐 Starting server..."
echo "📚 API Docs will be available at: http://localhost:8000/docs"
echo ""

# Run with uvicorn directly
uvicorn main:app --host 0.0.0.0 --port 8000 --reload --log-level info

echo ""
echo "👋 Server stopped"
