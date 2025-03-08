from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import premium_users
from config.config import OWNER_ID, FORCE_SUB_CHANNEL, AUTO_DELETE_TIME

@Client.on_message(filters.command("add_premium") & filters.user(OWNER_ID))
async def add_premium(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: /add_premium <user_id>")
    
    user_id = int(message.command[1])
    premium_users.insert_one({"user_id": user_id})

    await message.reply_text(f"✅ User `{user_id}` added to Premium!")

@Client.on_message(filters.command("remove_premium") & filters.user(OWNER_ID))
async def remove_premium(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("❌ Usage: /remove_premium <user_id>")
    
    user_id = int(message.command[1])
    premium_users.delete_one({"user_id": user_id})

    await message.reply_text(f"✅ User `{user_id}` removed from Premium!")

@Client.on_message(filters.command("list_premium") & filters.user(OWNER_ID))
async def list_premium(client, message: Message):
    users = premium_users.find()
    if users.count() == 0:
        return await message.reply_text("❌ No Premium users found.")
    
    text = "👑 **Premium Users:**\n"
    for user in users:
        text += f"🔹 `{user['user_id']}`\n"

    await message.reply_text(text)
