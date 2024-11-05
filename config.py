from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","21803165"))
API_HASH = getenv("API_HASH","05e5e695feb30e25bef47484cc006da7")

BOT_TOKEN = getenv("BOT_TOKEN","7732529579:AAFHBwOo1tsX5rqUToaRcCwgG_iilgRv2bE")
OWNER_ID = int(getenv("OWNER_ID","7070591202"))

MONGO_DB_URI = getenv("mongodb+srv://Somu:Somu@somu.xbkiklu.mongodb.net/?retryWrites=true&w=majority&appName=Somu")
MUST_JOIN = getenv("MUST_JOIN","somueditingzone")