import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "5716954283:AAESJMdwVbJY89-dXt4MhZv2ShyzmfGWGVs"

def cat(update, context):
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url).json()
    cat_image_url = response[0]['url']
    update.message.reply_photo(photo=cat_image_url)

def unknown(update, context):
    update.message.reply_text("I don't know.")

def main():
    updater = Updater(token=TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("cat", cat))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, unknown))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
