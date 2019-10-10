import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import Config


def start(update, context):
    message = "<h1>Hello</h1><p>This is echo bot</p>"
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)

def echo(update, context):
    print('Get message: {}\nFrom the user: {}'.format(update.message.text, update.message.from_user.first_name))
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(token=Config.bot_token, use_context=True, request_kwargs=Config.request_kwargs)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
