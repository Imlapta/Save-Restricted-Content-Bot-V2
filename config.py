# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29773843"))
API_HASH = getenv("API_HASH", "8b40e91c29a00fecb905d6eb6aee2b3b")
BOT_TOKEN = getenv("BOT_TOKEN", "7673624928:AAE-kr8fIglNA8qy91KM99P-7hbTHUrRoKA")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7766420864").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ganeshchouhan7877:rdX15xt2odwLpXVEdj@cluster0.8r5un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-4602402224")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002332500468"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
