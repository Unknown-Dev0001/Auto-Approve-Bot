import os
from typing import List

API_ID = os.environ.get("API_ID", "")
API_HASH = os.environ.get("API_HASH", "")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# Support multiple admins
admin_raw = os.environ.get("ADMIN", "").strip()
ADMIN: List[int] = list(map(int, admin_raw.split())) if admin_raw else []

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "0"))
NEW_REQ_MODE = os.environ.get("NEW_REQ_MODE", "False").lower() == "true"

DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "")

# Force-subscription settings
IS_FSUB = os.environ.get("IS_FSUB", "False").lower() == "true"
auth_channels_raw = os.environ.get("AUTH_CHANNEL", "").strip()
AUTH_CHANNELS: List[int] = list(map(int, auth_channels_raw.split())) if auth_channels_raw else []
