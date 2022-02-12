from platform import python_version as y
from telegram import __version__ as o
from pyrogram import __version__ as z
from telethon import __version__ as s
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
from SiestaRobot import pbot
from SiestaRobot.utils.errors import capture_err
from SiestaRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text message to make carbon.`")
    m = await message.reply_text("`Preparing Carbon`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


MEMEK = "https://telegra.ph/file/6771f4f67dc83a6d3a8c8.jpg"

@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=MEMEK,
        caption=f"""✨ **ʜᴇʏ ɪ'ᴍ ᴋɪᴢɪᴇ ʀᴏʙᴏᴛ** ✨ 

**ᴏᴡɴᴇʀ ʀᴇᴘᴏ : [ᴍᴀɴɴʏ ➖🇮🇳 </>](https://t.me/IMANUEL_MANNY)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀsɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{z}`

**ᴡᴀɴᴛ ʀᴇᴘᴏ ᴛʜᴀɴ ᴋɪɴᴅʟʏ ᴄᴏɴᴛᴀᴄᴛ ʙᴇʟᴏᴡ.**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ᴏᴡɴᴇʀ {ʀᴇᴘᴏ}", url="https://t.me/IMANUEL_MANNY"), 
                    InlineKeyboardButton(
                        "sᴜᴘᴘᴏʀᴛ", url="https://t.me/Kiziemusic")
                ]
            ]
        )
    )
