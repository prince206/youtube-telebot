# Telegram Bot for Summarizing youtube video by pasting video link

This is a Telegram bot that can summarize audio transcriptions using the OpenAI API and Eden AI API. The bot can download audio from YouTube videos, transcribe the audio to text, and then summarize the text using the APIs.
 
 ## Requirements
 
 - Python 3
 - `requests` library
 - `openai` library
 - `yt-dlp` command-line tool (for downloading YouTube videos)
 - Telegram Bot API token
 - OpenAI API key
 - Eden AI API key
 
 ## Usage
 
 1. Clone this repository: `git clone https://github.com/prince206/youtube-telebot.git`
 2. Install dependencies: `pip install -r requirements.txt`
 3. Set environment variables for your Telegram Bot API token and OpenAI API key:
 
 ```
 export TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
 export OPENAI_API_KEY="YOUR_OPENAI_API_KEY"
 ```
 
 4. Set environment variable for your Eden AI API key:
 
 ```
 export EDEN_AI_API_KEY="YOUR_EDEN_AI_API_KEY"
 ```
 
 5. Start the bot: `python telewhisp.py`
 
 ## Commands
 
 The bot supports the following commands:
 
 - `/sum <YouTube URL>` - Downloads audio from a YouTube video, transcribes it to text, summarizes the text using the OpenAI and Eden AI APIs, and replies with a summary of the text.
 
 ## License
 
 This project is licensed under the MIT License - see the LICENSE file for details.
