from flask import Flask
from threading import Thread
from pyrogram import Client
from config.config import BOT_TOKEN, API_ID, API_HASH

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=8080)

bot = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

if __name__ == "__main__":
    Thread(target=run).start()
    bot.run()
