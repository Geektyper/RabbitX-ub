from pyrogram.types import InlineQueryResultPhoto as IQRP
from config import STUFF
from .plugins import SPARE, HELP_TEXT, HELP_MARKUP
from client import BOT

if not STUFF.HELP_PIC:
    HELP_PIC = SPARE
else:
    HELP_PIC = STUFF.HELP_PIC

ans = [IQRP(photo_url=HELP_PIC, thumb_url=SPARE, title="Help", description="Help Module [ʀᴀʙʙɪᴛx]", caption=HELP_TEXT, reply_markup=HELP_MARKUP)]

@BOT.on_inline_query()
async def inl(_, i):
    text = i.query.lower()
    try:
        if text == "inline_help":
            await _.answer_inline_query(i.id, results=ans, cache_time=0)     
    except Exception as e:
        print(e)