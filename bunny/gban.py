from .Database.gban import *
from pyrogram import Client, filters
from .verify import verify
from . import hl, get_id_and_args

@Client.on_message(filters.command("gban", hl))
async def muter(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id, args = await get_id_and_args(_, m)
    except:
        return await m.reply("Invalid User !")
    if await verify(id):
        return await m.reply("Can't gban sudo users !")
    if await is_gbanned(id):
        return await m.reply("User is already gbanned !")
    await gban(id)
    await m.reply(f"Gbanned `{id}`.")

@Client.on_message(filters.command("ungban", hl))
async def unmuter(_, m):
    if not await verify(m.from_user.id):
        return
    try:
        id, args = await get_id_and_args(_, m)
    except:
        return await m.reply("Invalid User !")
    if not await is_gbanned(id):
        return await m.reply("User haven't been gbanned !")
    await ungban(id)
    await m.reply(f"Ungbanned `{id}`.")

@Client.on_message(group=11)
async def cwf(_, m):
    if not m.from_user:
        return
    id = m.from_user.id
    if not await is_gbanned(id):
        return
    try:
        await _.ban_chat_member(m.chat.id, id)
        return await m.reply("User have been banned due to gban !")
    except:
        return