from bunny.Database.sudo import is_sudo
from config import DEV
from .data import RabbitX 
LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + RabbitX 

async def verify(id):
    if not await is_sudo(id):
        if not id in LEGENDS:
            return False
    return True