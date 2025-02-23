import os
import logging
import random
import threading
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from pymongo import MongoClient
from health_check import start_health_check

# 🔰 Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 🔰 Environment Variables
API_ID = int(os.getenv("API_ID", "27788368"))
API_HASH = os.getenv("API_HASH", "9df7e9ef3d7e4145270045e5e43e1081")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7725707727:AAFtx6Sy-q6GgB9eaPoN2-oYPx2D6hjnc1g")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aarshhub:6L1PAPikOnAIHIRA@cluster0.6shiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", "-1002492623985"))
OWNER_ID = int(os.getenv("OWNER_ID", "6860316927"))
FORCE_SUBSCRIBE = os.getenv("FORCE_SUBSCRIBE", "True").lower() == "true"
FSUB_CHANNEL_ID = os.getenv("FSUB_CHANNEL_ID", "-1002490575006")

# 🔰 Initialize Bot & Database
bot = Client("video_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
mongo = MongoClient(MONGO_URL)
db = mongo["VideoBot"]
collection = db["videos"]

# 🔰 Function to fetch & send a random video
async def send_random_video(client, chat_id):
    video_docs = list(collection.find())
    if not video_docs:
        await client.send_message(chat_id, "⚠ No videos available. Use /index first!")
        return
    random_video = random.choice(video_docs)
    await client.forward_messages(chat_id=chat_id, from_chat_id=CHANNEL_ID, message_ids=random_video["message_id"])

# 🔰 Command to index videos (Owner Only)
@bot.on_message(filters.command("index") & filters.user(OWNER_ID))
async def index_videos(client, message):
    await message.reply_text("🔄 Indexing videos... This may take some time.")

    indexed_count = 0
    message_ids = list(range(1, 1001))
    messages = await client.get_messages(CHANNEL_ID, message_ids)

    for msg in messages:
        if msg and msg.video:
            collection.update_one(
                {"message_id": msg.id},
                {"$set": {"message_id": msg.id}}, 
                upsert=True
            )
            indexed_count += 1

    if indexed_count > 0:
        await message.reply_text(f"✅ Indexing completed! {indexed_count} videos added.")
        await client.send_message(OWNER_ID, f"📢 Successfully indexed {indexed_count} videos!")
    else:
        await message.reply_text("⚠ No videos found in the channel. Make sure the bot has access!")

# 🔰 Start Command with Reply Keyboard Button
@bot.on_message(filters.command("start"))
async def start(client, message):
    if FORCE_SUBSCRIBE:
        user_id = message.chat.id
        try:
            chat_member = await client.get_chat_member(FSUB_CHANNEL_ID, user_id)
            if chat_member.status not in ["member", "administrator", "creator"]:
                await message.reply_text(
                    "🚨 You must join our channel to use this bot!\n\n"
                    f"👉 [Join Channel](https://t.me/{FSUB_CHANNEL_ID})",
                    disable_web_page_preview=True
                )
                return
        except:
            pass  

    keyboard = ReplyKeyboardMarkup([["🎥 Get Random Video"]], resize_keyboard=True, one_time_keyboard=False)
    await message.reply_text("Welcome! Click the button below to get a random video:", reply_markup=keyboard)

# 🔰 Handle "🎥 Get Random Video" Button Click
@bot.on_message(filters.text & filters.regex("🎥 Get Random Video"))
async def handle_random_video(client, message):
    await send_random_video(client, message.chat.id)

# 🔰 Run the Bot
if __name__ == "__main__":
    threading.Thread(target=start_health_check, daemon=True).start()
    bot.run()
