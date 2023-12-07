from config import TOKENS, API
from pyrogram import Client

if TOKENS.BOT_TOKEN:
    BOT = Client(":BOT:", api_id=API.API_ID, api_hash=API.API_HASH, bot_token=TOKENS.BOT_TOKEN)
else:
    BOT = None

if TOKENS.STRING_SESSION:
    bunny = Client(":bunny", api_id=API.API_ID, api_hash=API.API_HASH, session_string=TOKENS.STRING_SESSION)