from pyrogram import Client, filters
from config import STUFF 
from . import hl

@Client.on_message(filters.command('id',  hl) & filters.me)
async def find_id(client, message):
    if message.reply_to_message is None:
        await message.edit(f"**__๏ Chat ID »__** `{message.chat.id}`")
    else:
        await message.edit(f"**__๏ User ID »**__ `{message.reply_to_message.from_user.id}`\n**__๏ Chat ID »**__ `{message.chat.id}`")