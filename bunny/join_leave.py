from config import DEV
from .data import RabbitX 
from .verify import verify
from pyrogram import Client, filters
from . import hl

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + RabbitX

@Client.on_message(filters.command("leave", hl))
async def leave(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id = int(m.text.split()[1])
    except:
        id = m.chat.id
    await m.reply("LEFT CHAT  ")
    await _.leave_chat(id)

@Client.on_message(filters.command("join", hl))
async def joiner(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id = int(m.text.split()[1])
    except:
        try:
            id = m.text.split()[1]
        except:
            return await m.reply(f"{hl}join [username|ID]")
    try:
        await _.join_chat(id)
        await m.reply("JOINED CHAT SUCCESSFULLY")
    except:
        await m.reply("Invalid username or ID")