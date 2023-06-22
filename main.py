import os

from telegram_bot.bot import start_bot

if __name__ == '__main__':
    token = os.environ.get('TELEGRAM_TOKEN')
    if token:
        start_bot(token)
