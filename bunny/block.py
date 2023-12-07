from bunny.helpers.basic import edit_or_reply
from bunny.utils.misc import extract_user
from pyrogram import Client, filters
from . import hl
from client import bunny as Client
from pyrogram.types import Message

@Client.on_message(filters.command(["block"], hl) & filters.me)
async def block(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await edit_or_reply(message, "`ρяσ¢єѕѕιиg...⚡`")
    if not user_id:
        return await message.edit(
            "**__give ID/Username or reply to user message to block..!!**__"
        )
    if user_id == client.me.id:
        return await bunny.edit("**__i can't ban myself lol..!!**__.")
    await client.block_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"__**๏ {geek} Blocked Successfully**__")