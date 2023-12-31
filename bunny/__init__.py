import time
from config import STUFF , API , TOKENS
from pyrogram import Client, filters
from datetime import datetime

from aiohttp import ClientSession

hl = STUFF.COMMAND_HANDLER

startTime = time.time()

async def get_id_and_args(_, m):
    if m.reply_to_message:
        id = m.reply_to_message.from_user.id
        if len(m.command) != 1:
            args = m.text.split(None, 1)[1]
        else:
            args = None
    else:
        if len(m.command) > 1:
            if len(m.command) < 3:
                args = None
            else:
                args = m.text.split(None, 2)[2]
            try:
                id = int(m.text.split()[1])
            except:
                pass
        if m.entities:
            if len(m.command) < 3:
                args = None
            else:
                args = m.text.split(None, 2)[2]
            for x in m.entities:
              if x.type.name == "MENTION":
                txt = m.text.split()[1]
                if txt[0] != "@":
                    id = None
                else:
                    try:
                        id = (await _.get_users(txt)).id
                    except:
                        id = None
              elif x.type.name == "TEXT_MENTION":
                id = x.user.id
    return id, args

app2 = Client(
    "bunny",
    api_id=API.API_ID,
    api_hash=API.API_HASH,
    session_string=str(TOKENS.STRING_SESSION),
)
aiosession = ClientSession()