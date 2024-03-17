import httpx
import os
import config 
from VIPMUSIC import app
from pyrogram import Client, filters
import aiofiles, aiohttp, requests


async def load_image(image: str, link: str):
    os.makedirs(os.path.dirname(image), exist_ok=True)  # Fix: Create directory if it doesn't exist
    async with aiohttp.ClientSession() as session:
        async with session.get(link) as resp:
            if resp.status == 200:
                f = await aiofiles.open(image, mode="wb")
                await f.write(await resp.read())
                await f.close()
                return image
            return None  # Fix: Return None instead of the image path


@app.on_message(filters.command("getdraw", prefixes="/"))
async def draw_image(client, message):
    chat_id = message.chat.id
    if message.sender_chat:
        user_id = message.sender_chat.id
    else:
        user_id = message.from_user.id
    replied = message.reply_to_message
    if not config.DEEP_API:
        return await message.reply_text("I can't upscale !")
    if replied:
        if replied.text:
            query = replied.text
    elif not replied:
        if len(message.text) < 2:
            return await message.reply_text("Please give a text or reply to a text !")
        query = message.text.split(None, 1)[1]
    aux = await message.reply_text("Please Wait ...")
    image = f"cache/{user_id}_{chat_id}_{message.id}.png"  # Fix: Modified image path
    data = requests.post(
        "https://api.deepai.org/api/text2img",
        data={
            'text': query,
            'grid_size': '1',
            'image_generator_version': 'hd',
        },
        headers={'api-key': config.DEEP_API}
    ).json()
    image_link = data.get("output_url")  # Fix: Use .get() method to handle potential missing key
    if not image_link:
        return await aux.edit("Failed to generate image, please try again.")
    downloaded_image = await load_image(image, image_link)
    if not downloaded_image:
        return await aux.edit("Failed to download image, please try again.")
    await aux.delete()
    await message.reply_photo(downloaded_image, caption=query)
