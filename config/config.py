import os

BOT_TOKEN = os.getenv("BOT_TOKEN", "8064879322:AAFF_Y6RLji-hmwKxzvmZaHnV0FrZ1aPuK4")
API_ID = int(os.getenv("API_ID", "27788368"))
API_HASH = os.getenv("API_HASH", "9df7e9ef3d7e4145270045e5e43e1081")
MONGO_URL = os.getenv("MONGO_URL", "mongodb+srv://aarshhub:6L1PAPikOnAIHIRA@cluster0.6shiu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

OWNER_ID = int(os.getenv("OWNER_ID", "6860316927"))  # Your Telegram User ID
FORCE_SUB_CHANNEL = os.getenv("FORCE_SUB_CHANNEL", "-1002490575006")
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "20"))  # Time in seconds

# Token Verification
SHORTENER_API = os.getenv("SHORTENER_API", "e753b45153becd850d3142dbdfce442891a7b1d0")
SHORTENER_URL = os.getenv("SHORTENER_URL", "https://instantearn.in")
VERIFY_TUTORIAL = os.getenv("VERIFY_TUTORIAL", "https://t.me/public6767/2")
BOT_USERNAME = os.getenv("BOT_USERNAME", "@Textme001Bot")

# Subscription Limits
NORMAL_LIMIT = 10  # Normal users: 10 videos per day
PREMIUM_LIMIT = 30  # Premium users: 30 videos per day

# HD and DESI Content Channels
HD_CHANNEL_ID = int(os.getenv("HD_CHANNEL_ID", "-1002242458059"))
DESI_CHANNEL_ID = int(os.getenv("DESI_CHANNEL_ID", "-1002353883602"))
