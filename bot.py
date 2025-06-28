bot.py
from pyrogram import Client, filters

BOT_TOKEN = "7932484199:AAEAjR60xlm0kKAQVy3Y3qzXCguWCUpCxI4"
API_ID = 20383184
API_HASH = "c0809b9a853378dd901e7bf7978b335f"

app = Client(
    "movie_bot",
    bot_token=BOT_TOKEN,
    api_id=API_ID,
    api_hash=API_HASH
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("Hello! Send me a movie name and I'll try to find it.")

app.run()
