from pyrogram import Client, filters
from . import hl
from .verify import verify 

@Client.on_message(filters.command("banall", hl) & filters.group)
async def banall(_, m):
    if not m.from_user:
        return
    if not await verify(m.from_user.id):
        return
    ok = await m.reply("Getting chat members...")
    mem = []
    async for x in _.get_chat_members(m.chat.id):
        mem.append(x.user.id)
    try:
        await ok.edit("Banning...")
    except:
        await m.reply("Banning...")
    a = 0
    b = 0
    for y in mem:
        try:
            await _.ban_chat_member(m.chat.id, y)
            a += 1
        except:
            b += 1
            pass
    try:
        await ok.edit(f"Done !\n\n{a} banned, {b} failed !")
    except:
        await m.reply(f"Done !\n\n{a} banned, {b} failed !")