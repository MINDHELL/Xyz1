from pyrogram import Client
from config.config import BOT_TOKEN, API_ID, API_HASH

bot = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

bot.run()
