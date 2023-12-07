from pyrogram import Client, filters
import requests
import os
from . import  hl

@Client.on_message(filters.command("webss", hl) & filters.me)
async def webshot(client, message):
    try:
        user_link = message.command[1]
        await message.edit("`тяуιиg тσ ¢яєαтє ѕ¢яєєиѕнσт...⚡`")
        try:
            full_link = f"https://webshot.deam.io/{user_link}/?width=1920&height=1080?delay=2000?type=png"
            await client.send_photo(message.chat.id, full_link, caption=f"**__๏ Screenshot of the page »__**** `{user_link}`")
        except Exception as dontload:
            await message.edit(f"𝕲𝖊𝖙𝖙𝖎𝖓𝖌 𝖘𝖈𝖗𝖊𝖊𝖓𝖘𝖍𝖔𝖙 𝖋𝖗𝖔𝖒 𝖌𝖎𝖛𝖊𝖓 𝖜𝖊𝖇𝖘𝖎𝖙𝖊...")
            full_link = f"https://mini.s-shot.ru/1920x1080/JPEG/1024/Z100/?{user_link}"
            await client.send_photo(message.chat.id, full_link, caption=f"**__๏ Screenshot of the page »__** `{user_link}`")
        await message.delete()
    except Exception as error:
        await message.delete()
        await client.send_message(
            message.chat.id, f"**__» ᴛʜɪs ɪs ɴᴏᴛ ᴀ ᴠᴀʟɪᴅ ᴜʀʟ...__**"
        )