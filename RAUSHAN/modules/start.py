# Don't remove This Line From Here.
# Telegram :- @ll_ALPHA_BABY_lll

import random
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import EMOJIOS, IMG, STICKER
from RAUSHAN import BOT_NAME, AMBOT, dev
from RAUSHAN.database.chats import add_served_chat
from RAUSHAN.database.users import add_served_user
from RAUSHAN.modules.helpers import (
    CLOSE_BTN,
    DEV_OP,
    HELP_BTN,
    HELP_BUTN,
    HELP_READ,
    HELP_START,
    SOURCE_READ,
    START,
)


@dev.on_message(filters.command(["start", "aistart"]) & ~filters.bot)
async def start(_, m: Message):
    try:
        user = m.from_user
        user_id = user.id
        first_name = user.first_name

        print("User object:", user)
        print("User name:", first_name)

        await add_served_user(user_id)
        await m.reply_chat_action("upload_photo")

        await m.reply_photo(
            photo=random.choice(IMG),
            caption=f"""**╭───────────────────⦿**
**│⛩️ ʜᴇʏ {first_name}, ɪ ᴀᴍ {BOT_NAME} •**
**├───────────────────⦿**
**│-꩜> ɪ ʀᴇᴀᴅ ʏᴏᴜʀ ᴍɪɴᴅ •**
**│⚡︎ ᴀɴ ᴀɪ ʙᴀsᴇᴅ ᴄʜᴀᴛʙᴏᴛ •**
**├───────────────────⦿**
**│ꑭ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs •**
**│☘ ɪ ᴄᴀɴ ʜᴇʟᴘ ʏᴏᴜ •**
**│✿ ғᴏʀ ᴀᴄᴛɪᴠᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ •**
**│✇ ᴜsᴀɢᴇ /chatbot [ᴏɴ/ᴏғғ] •**
**│𖣐 ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ʜᴇʟᴘ •**
**│🔥 24x7 ᴛɪᴍᴇ ᴏɴʟɪɴᴇ •**
**├───────────────────⦿**
**│🦊 ᴍᴀᴅᴇ ʙʏ...[˹ 𝐑𝐄𝐃 - 𝐋𝐈𝐍𝐄 ™ ˼](https://t.me/+QuuoMVb6zys0MDA1)♡**
**╰───────────────────⦿**""",
            reply_markup=InlineKeyboardMarkup(DEV_OP),
        )
    except Exception as e:
        print(f"Private start error: {e}")
        
    else:
        try:
            await add_served_chat(m.chat.id)
            await m.reply_photo(
                photo=random.choice(IMG),
                caption=START,
                reply_markup=InlineKeyboardMarkup(HELP_START),
            )
        except Exception as e:
            print(f"Group start error: {e}")


@dev.on_message(filters.command(["help"], prefixes=["+", ".", "/", "-", "?", "$"]))
async def help_handler(client: AMBOT, m: Message):
    if m.chat.type == ChatType.PRIVATE:
        try:
            await add_served_user(m.from_user.id)
            await m.reply_photo(
                photo=random.choice(IMG),
                caption=HELP_READ,
                reply_markup=InlineKeyboardMarkup(HELP_BTN),
            )
        except Exception as e:
            print(f"Help PM error: {e}")
    else:
        try:
            await add_served_chat(m.chat.id)
            await m.reply_photo(
                photo=random.choice(IMG),
                caption="**❍ ʜᴇʏ, ᴘᴍ ᴍᴇ ғᴏʀ ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs!**",
                reply_markup=InlineKeyboardMarkup(HELP_BUTN),
            )
        except Exception as e:
            print(f"Help group error: {e}")


@dev.on_message(filters.command("repo") & ~filters.bot)
async def repo(_, m: Message):
    try:
        await m.reply_text(
            text=SOURCE_READ,
            reply_markup=InlineKeyboardMarkup(CLOSE_BTN),
            disable_web_page_preview=True,
        )
    except Exception as e:
        print(f"Repo command error: {e}")


@dev.on_message(filters.new_chat_members)
async def welcome(_, m: Message):
    try:
        for member in m.new_chat_members:
            await m.reply_photo(photo=random.choice(IMG), caption=START)
    except Exception as e:
        print(f"Welcome error: {e}")
