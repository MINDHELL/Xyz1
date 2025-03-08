import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "your-bot-token")
API_ID = int(os.getenv("API_ID", "123456"))
API_HASH = os.getenv("API_HASH", "your-api-hash")
MONGO_URL = os.getenv("MONGO_URL", "your-mongodb-url")

OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  # Your Telegram User ID
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "your_channel_username")
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "300"))  # Time in seconds

# Token Verification
SHORTENER_API = os.getenv("SHORTENER_API", "")
SHORTENER_URL = os.getenv("SHORTENER_URL", "")
VERIFY_TUTORIAL = os.getenv("VERIFY_TUTORIAL", "")
BOT_USERNAME = os.getenv("BOT_USERNAME", "yourbotusername")

# Subscription Limits
NORMAL_LIMIT = 10  # Normal users: 10 videos per day
PREMIUM_LIMIT = 30  # Premium users: 30 videos per day

# HD and DESI Content Channels
HD_CHANNEL_ID = int(os.getenv("HD_CHANNEL_ID", "-100XXXXXXXX"))
DESI_CHANNEL_ID = int(os.getenv("DESI_CHANNEL_ID", "-100XXXXXXXX"))
