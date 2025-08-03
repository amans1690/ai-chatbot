from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from google import genai
import os
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Gemini client
client = genai.Client()

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Message is required'}), 400
        
        # Call Gemini API
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            contents=user_message
        )
        
        # Extract the response text
        bot_response = response.text if hasattr(response, 'text') else str(response)
        
        return jsonify({
            'response': bot_response,
            'status': 'success'
        })
        
    except Exception as e:
        print(f"Error in chat endpoint: {str(e)}")
        return jsonify({
            'error': 'An error occurred while processing your request',
            'details': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'service': 'chatbot-api'})

if __name__ == '__main__':
    # Check if GEMINI_API_KEY is set
    if not os.getenv('GEMINI_API_KEY'):
        print("Warning: GEMINI_API_KEY environment variable is not set!")
        print("Please set your Gemini API key before running the server.")
        print("You can set it by running: export GEMINI_API_KEY='your-api-key-here'")
    
    print("🚀 Starting Chatbot Server...")
    print("📱 Frontend will be available at: http://localhost:5000")
    print("🔧 API endpoint: http://localhost:5000/api/chat")
    
    app.run(debug=True, host='0.0.0.0', port=5000) 