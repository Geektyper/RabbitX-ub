from pyrogram import Client, filters, idle
from config import *
import time
import sys
from client import BOT
from geekgram import Geek
from config import DATABASE
if not BOT:
    print("BOT TOKEN NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
if not TOKENS.STRING_SESSION:
    print("MAIN STRING NOT FOUND, ADD IT TO INITIATE !")
    sys.exit()
END = Client(":END:", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION, plugins=dict(root="bunny"))

BOT.start()
print("Bot started, enable inline mode if not enabled !")
print("Starting User Clients...")
END.start()
try:
    END.join_chat("DevsX_Community")
except:
    pass
print("\nEND STARTED !")

print(f"\n\nUB STARTED SUCCESSFULLY !\nJoin @DevsX_Community")
idle()