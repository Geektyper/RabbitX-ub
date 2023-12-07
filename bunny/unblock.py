from bunny.helpers.basic import edit_or_reply
from bunny.utils.misc import extract_user
from pyrogram import Client, filters
from . import  hl
from client import bunny as Client
from pyrogram.types import Message


@Client.on_message(filters.command(["unblock"], hl) & filters.me)
async def unblock(client: Client, message: Message):
    user_id = await extract_user(message)
    bunny = await edit_or_reply(message, "`ρяσ¢єѕѕιиg...⚡`")
    if not user_id:
        return await message.edit(
            "__**give username/id or reply to a message to unblock that user..!!__**."
        )
    if user_id == client.me.id:
        return await bunny.edit("__ I can't unblock myself lol...!!__")
    await client.unblock_user(user_id)
    geek = (await client.get_users(user_id)).mention
    await message.edit(f"**__๏ {geek} unblocked successfully..!!**__")