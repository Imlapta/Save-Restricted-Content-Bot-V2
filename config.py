# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "3737117"))
API_HASH = getenv("API_HASH", "f466ca6ff400954d192ce0992ddf8b5d")
BOT_TOKEN = getenv("BOT_TOKEN", "7875472542:AAFGaPCwwvgzV-_11OaeQHVRWDLaK7QStOc")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1110590703").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://rrahuldhaker:7F6evbaKu8m7Ybr5@cluster0.w5kvs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
