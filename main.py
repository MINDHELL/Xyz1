import os
from flask import Flask
from threading import Thread
from pyrogram import Client

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize Pyrogram Bot
bot = Client(
    "mybot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Flask Health Check
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!", 200

def run_flask():
    app.run(host="0.0.0.0", port=8080)

# Start Flask in a separate thread
Thread(target=run_flask).start()

# Run the bot
bot.run()
