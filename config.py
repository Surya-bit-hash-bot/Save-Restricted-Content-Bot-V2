# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "20478011"))
API_HASH = getenv("API_HASH", "0e4dcf39643e83c3c174a0d2370e5b4a")
BOT_TOKEN = getenv("BOT_TOKEN", "7077374297:AAGgxSqJOrJ5GR8E3iiphrAzpL1FT1RW3Fk")
OWNER_ID = list(map(int, getenv("OWNER_ID", "2061656269").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://suryagupta1928:6thfnQ3AxzK6VJUA@cluster0.6ppqasw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002306621324")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002447666114"))
