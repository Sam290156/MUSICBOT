import asyncio
import sys

from motor import motor_asyncio
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

from ElinaRobot import MONGO_DB_URI, log
from ElinaRobot.conf import get_int_key, get_str_key

MONGO_PORT = get_int_key("27017")
MONGO_DB_URI = get_str_key("MONGO_DB_URI")
MONGO_DB = "ElinaRobot"


client = MongoClient()
client = MongoClient(MONGO_DB_URI, MONGO_PORT)[MONGO_DB]
motor = motor_asyncio.AsyncIOMotorClient(MONGO_DB_URI, MONGO_PORT)
db = motor[MONGO_DB]
db = client["ElinaRobot"]
try:
    asyncio.get_event_loop().run_until_complete(motor.server_info())
except ServerSelectionTimeoutError:
    sys.exit(log.critical("Β» π²π°π½'π π²πΎπ½π½π΄π²π ππΎ πΌπΎπ½πΆπΎπ³π± π΄ππΈππΈπ½πΆ β’β’β’"))
