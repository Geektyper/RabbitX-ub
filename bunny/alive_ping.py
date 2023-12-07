import time
from . import startTime
from config import STUFF, DEV
from .verify import verify
from pyrogram import Client, filters

PIC = STUFF.ALIVE_PIC if STUFF.ALIVE_PIC else "https://telegra.ph//file/3bc88e0963c045d0219e2.jpg"

OWNER = DEV.OWNER_ID

hl = STUFF.COMMAND_HANDLER

form = """

𝗥𝗔𝗕𝗕𝗜𝗧𝗫 𝐁𝐎𝐓 

┏━━━━━━✦❘༻༺❘✦━━━━━━┓
┃ 𝗥𝗔𝗕𝗕𝗜𝗧𝗫 𝐁𝐎𝐓 : V2
┃ 𝐔𝐏𝐓𝐈𝐌𝐄 : {}
┃ 𝐎𝐖𝐍𝐄𝐑 : {}
┗━━━━━━✦❘༻༺❘✦━━━━━━┛
┏━━━━━━✦❘༻༺❘✦━━━━━━┓
┃ ⁭⁫   𝐏𝐈𝐍𝐆 : `{}` ms   ┃
┗━━━━━━✦❘༻༺❘✦━━━━━━┛
  ↠━━━━━☬◆☬━━━━━↞

"""

TEXT = """

°____Pong____°

   🔸️ {}
   🔹️ 𝙼𝚢 𝙼𝚊𝚜𝚝𝚎𝚛 ~ {}
   🔸️ 𝗥𝗔𝗕𝗕𝗜𝗧𝗫 𝐁𝐎𝐓 : V2

"""

def grt(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

@Client.on_message(filters.command("ping", hl))
async def ping(_, m):
    if not await verify(m.from_user.id):
        return
    st = time.time()
    ok = await m.reply("`Checking...`")
    end = time.time()
    men = (await _.get_users(OWNER)).mention
    pong = str((end-st)*1000)[0:5]
    gtr = grt(int(time.time()-startTime))
    xD = ""
    xD += f"✥ 𝙊𝙬𝙣𝙚𝙧 :- {men}\n"
    xD += f"✥ 𝙋𝙞𝙣𝙜 :- {str((end-st)*1000)[0:5]}ms\n"
    xD += f"✥ 𝙐𝙗 𝘿𝙚𝙫 :- [Masters](t.me/RaBBiTXUserBot)\n"
    return await ok.edit(TEXT.format(pong, men))

@Client.on_message(filters.command("alive", hl))
async def aliver(_, m):
    if not await verify(m.from_user.id):
        return
    x = time.time()
    ok = await m.reply_photo(PIC, caption="`checking...`")
    x = str((time.time()-x)*1000)
    y = x.index(".")
    x = f"`{x[0:y+2]}`"
    upt = grt(int(time.time()-startTime))
    men = (await _.get_users(OWNER)).mention
    await ok.edit(form.format(upt, men, x))