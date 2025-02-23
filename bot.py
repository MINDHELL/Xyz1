import random
import logging
import threading
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pymongo import MongoClient
from health_check import start_health_check

import os

API_ID = int(os.getenv("API_ID", "27788368"))
API_HASH = os.getenv("API_HASH", "9df7e9ef3d7e4145270045e5e43e1081")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7725707727:AAFtx6Sy-q6GgB9eaPoN2-oYPx2D6hjnc1g")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aarshhub:6L1PAPikOnAIHIRA@cluster0.6shiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1002492623985"))
OWNER_ID = int(os.getenv("OWNER_ID", "6860316927"))
# Initialize bot & database
bot = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
mongo = MongoClient(MONGO_URL)
db = mongo["VideoBot"]
collection = db["videos"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to fetch and send a random video
async def send_random_video(client, chat_id):
    video_docs = list(collection.find())
    if not video_docs:
        await client.send_message(chat_id, "⚠ No videos available. Use /index first!")
        return

    random_video = random.choice(video_docs)
    await client.forward_messages(chat_id=chat_id, from_chat_id=CHANNEL_ID, message_ids=random_video["message_id"])

# Command to manually index videos (Owner only)
@bot.on_message(filters.command("index") & filters.user(OWNER_ID))
async def index_videos(client, message):
    await message.reply_text("🔄 Indexing videos... This may take a while.")
    
    indexed_count = 0
    async for msg in client.get_chat_history(CHANNEL_ID, limit=1000):
        if msg.video:
            collection.update_one(
                {"message_id": msg.message_id},
                {"$set": {"message_id": msg.message_id}},
                upsert=True
            )
            indexed_count += 1
            print(f"✅ Indexed video: {msg.message_id}")

    if indexed_count > 0:
        await message.reply_text(f"✅ Indexing completed! {indexed_count} videos added.")
    else:
        await message.reply_text("⚠ No videos found in the channel. Make sure the bot has access!")

# Start command with inline button
@bot.on_message(filters.command("start"))
async def start(client, message):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🎥 Get Random Video", callback_data="get_random_video")]
    ])
    await message.reply_text("Welcome! Click the button below to get a random video:", reply_markup=keyboard)

# Callback for random video
@bot.on_callback_query(filters.regex("get_random_video"))
async def random_video_callback(client, callback_query: CallbackQuery):
    await send_random_video(client, callback_query.message.chat.id)
    await callback_query.answer()

if __name__ == "__main__":
    threading.Thread(target=start_health_check, daemon=True).start()  # ✅ Start health check
    bot.run()
