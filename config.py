import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

MONGO_URI = os.getenv("MONGO_URI")

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

UPDATE_CHANNEL = os.getenv(
    "UPDATE_CHANNEL",
    "@YourUpdateChannel"
)

LOG_GROUP_ID = int(
    os.getenv("LOG_GROUP_ID", "0")
)

WELCOME_PHOTO = os.getenv(
    "WELCOME_PHOTO",
    ""
)

DEFAULT_MUTE_HOURS = int(
    os.getenv("DEFAULT_MUTE_HOURS", "24")
)

WARN_LIMIT = int(
    os.getenv("WARN_LIMIT", "3")
)

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN is missing")

if not MONGO_URI:
    raise ValueError("MONGO_URI is missing")

if not OWNER_ID:
    raise ValueError("OWNER_ID is missing")