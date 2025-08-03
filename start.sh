#!/bin/bash

echo "🤖 AI Chatbot Startup Script"
echo "=============================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip first."
    exit 1
fi

# Check if GEMINI_API_KEY is set
if [ -z "$GEMINI_API_KEY" ]; then
    echo "⚠️  Warning: GEMINI_API_KEY environment variable is not set!"
    echo "Please set your Gemini API key before running the server."
    echo "You can set it by running: export GEMINI_API_KEY='your-api-key-here'"
    echo ""
    read -p "Do you want to continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Install dependencies
echo "📦 Installing Python dependencies..."
pip3 install -r requirements.txt

# Start the server
echo "🚀 Starting the chatbot server..."
echo "📱 Frontend will be available at: http://localhost:5000"
echo "🔧 API endpoint: http://localhost:5000/api/chat"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 app.py 