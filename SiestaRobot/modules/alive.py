import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/887c1912704eb98f24c4a.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**ᴋᴏɴɪᴄʜɪᴡᴀ [{event.sender.first_name}](tg://user?id={event.sender.id}), ɪ'ᴍ ᴋɪᴢɪᴇ ʀᴏʙᴏᴛ.** \n\n"
  TEXT += "🦋 **ɪ'ᴍ ᴡᴏʀᴋɪɴɢ sᴍᴏᴏᴛʜʟʏ** \n\n"
  TEXT += f"🦋 **ᴍʏ ᴍᴀsᴛᴇʀ : [MANNY➖🇮🇳](https://t.me/IMANUEL_MANNY)** \n\n"
  TEXT += f"🦋 **ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"🦋 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"🦋 **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ", "https://t.me/Kxtest_Bot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/Kiziemusic")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
