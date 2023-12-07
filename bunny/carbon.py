import asyncio
from io import BytesIO
from aiohttp import ClientSession
from pyrogram import Client, filters, enums
from pyrogram.types import Message, User
from . import hl
from bunny.helpers.basic import eor
from client import bunny as Client

aiosession = ClientSession()

def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.id

    elif not message.from_user.is_self:
        reply_id = message.id

    return reply_id

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@Client.on_message(filters.command("carbon", hl) & filters.me)
async def carbon_func(client: Client, message: Message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    bunny = await eor(message, "`ρяєραяιиg ¢αявσи...⚡`")
    carbon = await make_carbon(text)
    await bunny.edit("`υρℓσα∂ιиg...⚡`")
    await asyncio.gather(
        bunny.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            reply_to_message_id=ReplyCheck(message),
        ),
    )
    carbon.close()