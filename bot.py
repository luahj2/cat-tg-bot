import os
import requests
from telegram.ext import ApplicationBuilder, Updater, CommandHandler, MessageHandler, filters

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

async def cat(update, context):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url).json()
    cat_image_url = response[0]['url']
    await update.message.reply_photo(photo=cat_image_url)

async def unknown(update, context):
    await update.message.reply_text("I don't know.")

def main():
    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(CommandHandler("cat", cat))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, unknown))
    application.run_polling()

if __name__ == "__main__":
    main()
