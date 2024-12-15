# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29755134"))
API_HASH = getenv("API_HASH", "04922af1d83f05367c8781383bdc3665")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6350117077").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ganeshchouhan7877:rdX15xt2odwLpXVEdj@cluster0.8r5un.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002493840482")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002448672568"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "500"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
