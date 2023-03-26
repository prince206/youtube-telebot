import re
import requests
import json
import openai
import os
import subprocess
import openai
import telebot
from telebot import types


# Set Telegram Bot API Token
bot = telebot.TeleBot('your telegram bot token')

# Set OPENAI API Key
openai.api_key = 'your openai api key'


@bot.message_handler(commands=['sum'])
def summarize_text(message):
    try:
        # Get the URL from the message text
        url = message.text.split()[1]
 
        # Download Audio from YouTube Video
        cmd = f'yt-dlp -x --audio-format mp3 {url}'
        subprocess.run(cmd, shell=True)
        audiox = subprocess.check_output(cmd, shell=True).decode('utf-8')
        pattern = r"download] (.*) has already been downloaded"
        result = re.search(pattern, audiox)
 
        if result:
            answer = result.group(1)
            print(answer)
        filename = [f for f in os.listdir() if answer[-12:-2] in f][0]
        print(filename)
        # Transcribe Audio to Text
        with open(filename, 'rb') as f:
            transcript = str(openai.Audio.transcribe("whisper-1", f))
        with open('transcript.txt', 'w') as f:
            f.write(transcript)
        with open('transcript.txt', 'rb') as f:
            bot.send_document(message.chat.id, f)
        # Summarize Transcription using Eden AI API
        key = 'add your eden ai api key'
        headers = {"Authorization": "Bearer key"}
        url ="https://api.edenai.run/v2/text/summarize"
        
        payload={"providers": "openai", "language": "en", "text": transcript}

        response = requests.post(url, json=payload, headers=headers)

        result = json.loads(response.text)

        summary_text = result['openai']['result']
        print(summary_text)

        # Reply with Summary Text
        if summary_text == "":
            bot.reply_to(message, "Cannot Summarize Text. Please try again.")
        else:
            bot.reply_to(message, "Summary:\n\n" + summary_text)
    except Exception as e:
        bot.reply_to(message, e)
        
bot.polling()
