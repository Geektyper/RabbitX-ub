from pyrogram import Client, filters
from bunny.helpers.basic import eor
from . import hl
from bunny.utils.verify import verify
from bunny.utils.get_id import get_id
from bunny.utils.capsify import capsify
from bunny.Database.pm import *
from config import STUFF

RABBIT = STUFF.HELP_PIC
pm_watcher = [5]

TEXT = capsify("""Hey {} 👋, This is the PM Security of {} 👮!



Because of the  spam messages my master get all the time, he don't like to chat with "strangers" now!
So kindly  wait for his approval 🤗!


You have {} of warns! Be careful, if you've exceeded warn limit you'll be blocked 🛑!.

Current warnings : {}""")

@Client.on_message(filters.command("pmprotect", hl) & filters.me)
async def pmpro(_, m):
    x = await is_pm_on()
    try:
        tg = m.text.split()[1].lower()
    except:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if not tg in ["on", "off"]:
        return await eor(m, f"{hl}pmprotect [on | off]")
    if tg == "on":
        if x:
            return await eor(m, capsify("PM PROTECTION ALREADY ENABLED !"))
        await toggle_pm()
        if await limit() == 0:
            await update_warns(3)
        return await eor(m, capsify("PM PROTECTION ENABLED !"))
    if not x:
        return await eor(m, capsify("PM PROTECTION ISN'T ENABLED !"))
    await toggle_pm()
    return await eor(m, capsify("PM PROTECTION DISABLED !"))

@Client.on_message(filters.command(["approve", "disapprove", "a", "da", "allow", "disallow"], hl) & filters.me)
async def appro_dis(_, m):
    if str(m.chat.id)[0] == "-":
        try:
            id = await get_id(_, m)
        except:
            return await eor(m, capsify("REPLY OR GIVE ID !"))
    else:
        id = m.chat.id
    tg = m.text.split()[0][1]
    x = await is_approved(id)
    if tg == "d":
        if not x:
            return await eor(m, capsify("USER WASN'T APPROVED !"))
        await disapprove(id)
        return await eor(m, capsify("DISAPPROVED USER TO PM !"))
    if x:
        return await eor(m, capsify("USER ALREADY APPROVED !"))
    await approve(id) 
    await reset_warns(id)
    return await eor(m, capsify("USER APPROVED TO PM !"))

@Client.on_message(filters.command("setwarns", hl) & filters.me)
async def setter(_, m):
    try:
        count = int(m.text.split()[1])
    except:
        return await eor(m, f"{hl}setwarns [value]")
    if count == 0:
        return await eor(m, capsify("GIVE VALUE ABOVE 0 !"))
    await update_warns(count)
    await eor(m, capsify(f"PM WARNS SET TO {count} !"))

@Client.on_message(filters.private, group=pm_watcher)
async def cwf(_, m):
    if m.from_user.is_self:
        if await is_approved(m.chat.id) is False:
            await approve(m.chat.id)
            await m.reply(capsify("user approved to pm due to self messaging !"))
    if not await is_pm_on():
        return
    if await verify(_, m):
        return
    if await is_approved(m.from_user.id):
        return
    await add_warn(m.from_user.id)
    if await limit() <= await get_warns(m.from_user.id):
        await m.reply("GOOD BYE UNTIL MY MASTER ARRIVES !")
        await reset_warns(m.from_user.id)
        return await _.block_user(m.from_user.id)
    await m.reply_photo(RABBIT, caption=TEXT.format(m.from_user.first_name, (await _.get_me()).first_name, await limit(), await get_warns(m.from_user.id)))