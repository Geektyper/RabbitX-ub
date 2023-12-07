import requests
from pyrogram import Client, filters
from pyrogram.types import Message
from . import hl
from bunny.helpers.basic import get_text

@Client.on_message(filters.command("utweet", hl) & filters.me)
async def tweet(client: Client, message: Message):
    text = get_text(message)
    input_str = get_text(message)
    if text:
        if ":" in text:
            stark = input_str.split(":", 1)
        else:
            await message.edit(f"**๏ Usage »** `{hl}utweet username:text`")
            return
    if len(stark) != 2:
        await message.edit(f"**๏ Usage »** `{hl}utweet username:text`")
        return
    tony = stark[0]
    shiva = stark[1]
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={tony}&text={shiva}"
    seg = requests.get(url=url).json()
    tweet = seg["message"]
    await message.edit(f"`Wait I Am Tweeting...`")
    await client.send_photo(message.chat.id, tweet)
    await message.delete()