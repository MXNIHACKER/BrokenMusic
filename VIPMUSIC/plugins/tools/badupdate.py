from pyrogram import Client, filters
import requests
import random
import os
import re
import asyncio
import time
from VIPMUSIC import app

from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


app.on_message(
    filters.command("repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("source", "repo")
    & filters.group)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                 ]
            ]
        ),
    )

@app.on_message(
    filters.command("repo")
    & filters.private)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/712e28b6207db1448ac88.jpg",
        caption=f"""🦋 𝐂ʟɪᴄᴋ 𝐁ᴇʟᴏᴡ 𝐁ᴜᴛᴛᴏɴ 𝐓ᴏ 𝐆ᴇᴛ 𝐑ᴇᴘᴏ ❤️""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐌ᴜsɪᴄ  𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                [
                    InlineKeyboardButton(
                        "🗡️ 𝐏ʙx ᴜ  𝐑ᴇᴘᴏ  🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                ],
                 [
                    InlineKeyboardButton(
                        "🗡️ 𝐑ᴇᴘᴏ 🗡️", url=f"https://github.com/MXNIHACKER/BrokenMusic/fork")
                 ]
            ]
        ),
    )
