import os
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.utils.request import Request

logging.basicConfig(level=logging.INFO)

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm a movie downloader bot.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Just send me a movie name, and I'll try to download it for you!")

def download_movie(update, context):
    movie_name = update.message.text
    # Add your movie download logic here
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Downloading {movie_name}...")

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', help))
    dp.add_handler(MessageHandler(Filters.text, download_movie))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
