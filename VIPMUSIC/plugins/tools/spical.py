import os
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *
from logging import getLogger
from VIPMUSIC import app





LOGGER = getLogger(__name__)

class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}  # You can store additional information related to the chat
        # For example, self.data[chat_id]['some_key'] = 'some_value'

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

# ... (rest of your code remains unchanged)

# ... (FUCK you randi ke bacvhhe )

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chatname, id, uname):
    background = Image.open("VIPMUSIC/assets/wel2.png")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((825, 824))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('VIPMUSIC/assets/font.ttf', size=110)
    welcome_font = ImageFont.truetype('VIPMUSIC/assets/font.ttf', size=60)
    draw.text((2100, 1420), f'ID: {id}', fill=(12000, 12000, 12000), font=font)
    pfp_position = (1990, 435)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"

# FUCK you bhosadiwale 


@app.on_message(filters.command("welcome") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n⦿/wel [on|off]\n➤ᴀᴜʀ ʜᴀᴀɴ ᴋᴀɴɢᴇʀs ᴋᴀʀᴏ ᴀʙ ᴄᴏᴘʏ ʙʜᴏsᴀᴅɪᴡᴀʟᴇ\n➤sᴀʟᴏɴ ᴀᴜʀ ʜᴀᴀɴ sᴛʏʟɪsʜ ғᴏɴᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ɪɴ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.!\ᴀᴜʀ ʜᴀᴀɴ ᴀɢʀ ᴋʜᴜᴅ ᴋɪ ᴋᴀʀɴɪ ʜᴀɪ ᴛᴏ ɢᴀᴀɴᴅ ᴍᴀʀᴀᴏ ʙᴇᴛɪᴄʜᴏᴅ"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await app.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "on":
            if A:
                return await message.reply_text("Special Welcome Already Enabled")
            elif not A:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
        elif state == "off":
            if not A:
                return await message.reply_text("Special Welcome Already Disabled")
            elif A:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("Only Admins Can Use This Command")

# ... (copy paster teri maa ki chut  )

@app.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)  # Corrected this line
    if not A:
        return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await app.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "VIPMUSIC/assets/upic.png"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await app.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
**Wᴇʟᴄᴏᴍᴇ Tᴏ {member.chat.title}

🏘𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳

❍══════════════════════════❍

╔══════════════════
╠ ➤ 𝐍ᴀᴍᴇ 🖤 ◂⚚▸ {user.mention} ❤️🔐
╠ ➤ 𝐔ꜱᴇʀ 𝐈ᴅ 🖤 ◂⚚▸ {user.id} ❤️🧿
╠ ➤ 𝐔ꜱᴇʀɴᴀᴍᴇ 🖤 ◂⚚▸ @{user.username} ❤️🌎
╚══════════════════

❍══════════════════════════❍
    ┏━━━━━━━⛈━━━━━━━┓
    ✫ ᴛᴇʀɪ ᴍᴇʀɪ ᴅᴏꜱᴛɪ ɪᴛɴɪ
          ᴋʜᴀꜱ ʜᴏ ᴋᴇ ✤
     ✫ ᴅᴜɴɪʏᴀ ᴋᴀʜᴇ ᴋᴀᴀꜱʜ
          ᴀɪꜱᴀ ᴅᴏꜱᴛ ᴍᴇʀᴇ 
           ᴘᴀꜱꜱ ʜᴏ ✤
    ┗━━━━━━━⛱━━━━━━━┛
❍══════════════════════════❍
┏━━━━━━━━━━━━━━━━♡
✰ᴀɴʏ ᴘʀᴏʙʟᴇᴍ @admin     
┗━━━━━━━━━━━━━━━━♡
❍══════════════════════════❍
      ┏━━━━━━━━━━┓             
     ❤️  ✨ʀᴜʟᴇs  ✨❤️
      ┗━━━━━━━━━━┛
-----------------------------------------------------
┏━━━━━━━━━━━━━━━━━
┣ 𝟏 ✧ ᴅᴏɴᴛ ᴀʙᴜsɪɴɢ ❤️🤙
┣ 𝟐 ✧ ᴅᴏɴᴛ sᴘᴀᴍ 🥲❤️
┣ 𝟑 ✧ ʟɪɴᴋ ɴᴏᴛ ᴀʟʟᴏᴡ ❤️🙌
┣ 𝟒 ✧ ᴅᴏɴᴛ sᴇɴᴅ ᴀᴅᴜʟᴛ sᴛᴜғғ❤️👻
┗━━━━━━━━━━━━━━━━━     
    ----------------------------------------------------
     ♡︎ 🇬ɪᴠᴇ  🇷ᴇsᴘᴇᴄᴛ  ꨄ︎
              ꨄ︎ 🇹ᴀᴋᴇ  🇷ᴇsᴘᴇᴄᴛ ♡︎
    -----------------------------------------------------           
                   
        ꧁ ༺ 𝐓нαик 𝐘συ ༻ ꧂
❍══════════════════════════❍**
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"✰ ᴠɪᴇᴡ ɴᴇᴡ ᴍᴇᴍʙᴇʀ ✰", url=f"tg://openmessage?user_id={user.id}")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass

# ... (resfuxbk 

@app.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == app.me.id:
            await app.send_message(LOG_CHANNEL_ID, f"""
**Wᴇʟᴄᴏᴍᴇ Tᴏ {member.chat.title}

🏘𝐖ᴇʟᴄᴏᴍᴇ 𝐈ɴ 𝐍ᴇᴡ 𝐆ʀᴏᴜᴘ🥳

❍══════════════════════════❍

╔══════════════════
╠ ➤ 𝐍ᴀᴍᴇ 🖤 ◂⚚▸ {user.mention} ❤️🔐
╠ ➤ 𝐔ꜱᴇʀ 𝐈ᴅ 🖤 ◂⚚▸ {user.id} ❤️🧿
╠ ➤ 𝐔ꜱᴇʀɴᴀᴍᴇ 🖤 ◂⚚▸ @{user.username} ❤️🌎
╚══════════════════

❍══════════════════════════❍
    ┏━━━━━━━⛈━━━━━━━┓
    ✫ ᴛᴇʀɪ ᴍᴇʀɪ ᴅᴏꜱᴛɪ ɪᴛɴɪ
          ᴋʜᴀꜱ ʜᴏ ᴋᴇ ✤
     ✫ ᴅᴜɴɪʏᴀ ᴋᴀʜᴇ ᴋᴀᴀꜱʜ
          ᴀɪꜱᴀ ᴅᴏꜱᴛ ᴍᴇʀᴇ 
           ᴘᴀꜱꜱ ʜᴏ ✤
    ┗━━━━━━━⛱━━━━━━━┛
❍══════════════════════════❍
┏━━━━━━━━━━━━━━━━♡
✰ᴀɴʏ ᴘʀᴏʙʟᴇᴍ @admin     
┗━━━━━━━━━━━━━━━━♡
❍══════════════════════════❍
      ┏━━━━━━━━━━┓             
     ❤️  ✨ʀᴜʟᴇs  ✨❤️
      ┗━━━━━━━━━━┛
-----------------------------------------------------
┏━━━━━━━━━━━━━━━━━
┣ 𝟏 ✧ ᴅᴏɴᴛ ᴀʙᴜsɪɴɢ ❤️🤙
┣ 𝟐 ✧ ᴅᴏɴᴛ sᴘᴀᴍ 🥲❤️
┣ 𝟑 ✧ ʟɪɴᴋ ɴᴏᴛ ᴀʟʟᴏᴡ ❤️🙌
┣ 𝟒 ✧ ᴅᴏɴᴛ sᴇɴᴅ ᴀᴅᴜʟᴛ sᴛᴜғғ❤️👻
┗━━━━━━━━━━━━━━━━━     
    ----------------------------------------------------
     ♡︎ 🇬ɪᴠᴇ  🇷ᴇsᴘᴇᴄᴛ  ꨄ︎
              ꨄ︎ 🇹ᴀᴋᴇ  🇷ᴇsᴘᴇᴄᴛ ♡︎
    -----------------------------------------------------           
                   
        ꧁ ༺ 𝐓нαик 𝐘συ ༻ ꧂
❍══════════════════════════❍**
""")
    
