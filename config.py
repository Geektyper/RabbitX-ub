import os
from os import getenv

from dotenv import load_dotenv

load_dotenv()

PMPERMIT = getenv("PMPERMIT","ENABLE")

class API:
    API_ID = int(os.getenv("API_ID", "21455847"))
    API_HASH = os.getenv("API_HASH", "8362067b5445fd55efd6b70d78f97fbd")

class TOKENS:
    BOT_TOKEN = os.getenv("BOT_TOKEN", "6963593429:AAHV9tJ7Kbe1r99Q2iPaqXfT9lGy0WXLtrA")
    STRING_SESSION = os.getenv("STRING_SESSION", "BAGqvsEAbvm1EFPX2jmPWdG6Qc556BX86Tt2rgrpKDRdnMxoubgzaB3BTLZzmhiQLm9tglDJagpVpfHQb2RNUe3ODjzecqFVedWO0axreSSZa_kCdWCPQiLlliJAorwoSH7U8BvcPGwtozkb2JoDv4M8xP8Ky2YpS7iUyxODNE3E1jPPBvtIq8vTrvhL1j1DOKHrXwXc6tTi3-uOtg1S3GIK9uUh3NzIuAwVE1-p74cjXCVcBHq_XDPVExJ_dxwKQ4CkO_UHrm4l74P3_Vs7_8HmdxsGUw8cz6OAJ_fR-vGnJAlnVp38Ukyf03SPOFh-8UxAGY9mXKZm0ve51b5gOLAZgBM_mQAAAAGfUN2IAA")

class config:
    MONGO_DATABASE = os.getenv("MONGO_DATABASE","mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")
class DATABASE:
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://Alisha:Alisha123@cluster0.yqcpftw.mongodb.net/?retryWrites=true&w=majority")

class DEV:
    OWNER_ID = int(os.getenv("OWNER_ID", "6967844232"))

    # DONT EDIT THIS 
    SUDO_USERS = [] 
    # YOU CAN ADD SUDO USING /addsudo

class STUFF:
    PMPERMIT = os.getenv("PMPERMIT", None)
    ALIVE_PIC = os.getenv("ALIVE_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    HELP_PIC = os. getenv("HELP_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    START_PIC = os. getenv("START_PIC", "https://telegra.ph/file/ff88788a1ae767111d500.jpg")
    COMMAND_HANDLER = os. getenv("COMMAND_HANDLER", ".")
    ALLOW_PORN = os.getenv("ALLOW_PORN", True) # CHANGE 'True' TO 'False' IF YOU WANNA DISABLE PORN