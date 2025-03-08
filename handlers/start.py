from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config.config import VERIFY_TUTORIAL, BOT_USERNAME, FORCE_SUB_CHANNEL

@Client.on_message(filters.command("start"))
async def start(client, message: Message):
    buttons = [[
        InlineKeyboardButton("📽 HD CONTENT", callback_data="hd_content"),
        InlineKeyboardButton("📀 DESI CONTENT", callback_data="desi_content")
    ], [
        InlineKeyboardButton("ℹ About", callback_data="about"),
        InlineKeyboardButton("🛒 Buy Subscription", callback_data="buy")
    ]]

    if FORCE_SUB_CHANNEL:
        buttons.append([InlineKeyboardButton("🔔 Join Channel", url=f"https://t.me/{FORCE_SUB_CHANNEL}")])

    await message.reply_photo(
        photo="https://your-image-url.com/welcome.jpg",
        caption="👋 **Welcome!**\n\nSelect an option below:",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
