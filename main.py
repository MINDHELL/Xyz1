from pyrogram import Client
from config.config import BOT_TOKEN, API_ID, API_HASH

bot = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot.run()

from flask import Flask
import threading

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!", 200

def run_web():
    app.run(host="0.0.0.0", port=8080)

threading.Thread(target=run_web, daemon=True).start()
