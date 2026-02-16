from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 36838583
API_HASH = "f85a86130a46c3efcbac6ec874da0771"
BOT_TOKEN = "8249294921:AAE4rm6-YzzoJaUmR52HK2nk6GjxYkgKyr4"
CHANNEL_ID = -1003762194941

app = Client("filebot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# SAVE FILE
@app.on_message(filters.private & filters.incoming & (filters.photo | filters.document | filters.video | filters.audio))
async def save_file(client, message: Message):
    copied = await message.copy(CHANNEL_ID)
    link = f"https://t.me/{(await client.get_me()).username}?start={copied.id}"
    await message.reply_text(f"✅ File saved!\n\n🔗 Download Link:\n{link}")

# SEND FILE BACK WHEN LINK OPENED
@app.on_message(filters.command("start"))
async def send_file(client, message: Message):
    if len(message.command) > 1:
        file_id = int(message.command[1])
        await client.copy_message(
            chat_id=message.chat.id,
            from_chat_id=CHANNEL_ID,
            message_id=file_id
        )
    else:
        await message.reply_text("Send me a file to store permanently.")

app.run()

