# AI Chatbot Frontend

A modern, responsive web interface for an AI chatbot powered by Google's Gemini 2.5 Flash model.

## Features

- 🎨 **Modern UI**: Clean, responsive design with smooth animations
- 💬 **Real-time Chat**: Interactive chat interface with typing indicators
- 🔄 **Auto-resize**: Textarea automatically adjusts to content
- 📱 **Mobile-friendly**: Responsive design works on all devices
- 🧹 **Clear Chat**: One-click chat history clearing
- ⚡ **Fast**: Optimized for quick responses
- 🔒 **Secure**: Input sanitization and error handling

## Screenshots

The chatbot features a beautiful gradient design with:
- Header with bot avatar and clear chat button
- Message bubbles with user/bot avatars
- Auto-expanding input field with character counter
- Typing indicators during API calls
- Smooth animations and transitions

## Setup Instructions

### Prerequisites

1. **Python 3.7+** installed on your system
2. **Google Gemini API Key** - Get one from [Google AI Studio](https://makersuite.google.com/app/apikey)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**:
   ```bash
   export GEMINI_API_KEY="your-gemini-api-key-here"
   ```
   
   Or create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. **Run the server**:
   ```bash
   python app.py
   ```

5. **Open your browser** and go to:
   ```
   http://localhost:8080
   ```

## Project Structure

```
ai-chatbot/
├── app.py              # Flask backend server
├── index.html          # Main HTML file
├── styles.css          # CSS styles
├── script.js           # JavaScript functionality
├── requirements.txt    # Python dependencies
├── __main__.py         # Original CLI chatbot
└── README.md          # This file
```

## API Endpoints

- `GET /` - Serves the main HTML page
- `POST /api/chat` - Chat endpoint that calls Gemini API
- `GET /api/health` - Health check endpoint

## Features

- **Markdown Support**: Bot responses are formatted with proper markdown rendering
- **Rich Text**: Headers, lists, bold, italic, code blocks, and links are properly styled
- **Responsive Design**: Works perfectly on desktop and mobile devices

## Usage

1. **Start a conversation**: Type your message in the input field
2. **Send messages**: Press Enter or click the send button
3. **Multi-line messages**: Use Shift+Enter for new lines
4. **Clear chat**: Click the trash icon in the header
5. **Character limit**: 2000 characters per message

## Customization

### Styling
- Edit `styles.css` to customize colors, fonts, and layout
- The design uses CSS custom properties for easy theming

### Functionality
- Modify `script.js` to add new features
- Update the API endpoint in `app.py` if needed

### Backend
- The Flask server in `app.py` handles API calls to Gemini
- Add authentication, rate limiting, or other features as needed

## Troubleshooting

### Common Issues

1. **API Key Error**:
   - Make sure `GEMINI_API_KEY` is set correctly
   - Check that your API key is valid and has sufficient quota

2. **Port Already in Use**:
   - Change the port in `app.py` line 58
   - Or kill the process using the port

3. **CORS Issues**:
   - The server includes CORS headers, but check browser console for errors
   - Ensure you're accessing via `http://localhost:5000`

4. **Module Not Found**:
   - Run `pip install -r requirements.txt` to install dependencies

### Debug Mode

The server runs in debug mode by default. Check the terminal for detailed error messages.

## Development

### Adding New Features

1. **Frontend**: Edit `script.js` and `styles.css`
2. **Backend**: Modify `app.py` for new API endpoints
3. **Styling**: Update `styles.css` for visual changes

### Testing

- Test the API directly: `curl -X POST http://localhost:8080/api/chat -H "Content-Type: application/json" -d '{"message":"Hello"}'`
- Check browser console for JavaScript errors
- Monitor server logs in the terminal

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests! 