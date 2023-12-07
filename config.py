import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()

PMPERMIT = getenv("PMPERMIT","ENABLE")

class API:
    API_ID = int(os.getenv("API_ID", ""))
    API_HASH = os.getenv("API_HASH", "")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "")
    STRING_SESSION = os.getenv("STRING_SESSION", "")

class config:
    MONGO_DATABASE = os.getenv("MONGO_DATABASE","")
class DATABASE:
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", ""))

    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    PMPERMIT = os.getenv("PMPERMIT", None)
    ALIVE_PIC = os.getenv("ALIVE_PIC", "")
    HELP_PIC = os. getenv("HELP_PIC", "")
    START_PIC = os. getenv("START_PIC", "")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", "!")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN