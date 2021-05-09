from telegram.ext import Updater,CommandHandler
from telegram.ext import MessageHandler,Filters,InlineQueryHandler
import logging
import telegram

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

bot = telegram.Bot(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE')

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello , Thanks for choosing us!!")

    context.job_queue.run_repeating(callback_minute, interval=1, first=3, context=update.message.chat_id)

def stop_timer(update, context):
    bot.send_message(chat_id=update.message.chat_id, text='Stoped!')
    context.job_queue.stop()

def callback_minute(context):
    chat_id = context.job.context
    print(chat_id)
    context.bot.send_message(chat_id=chat_id, text="Hi User, Add Fund to your account to start trading")

def main():
    updater = Updater('1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE', use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start, pass_job_queue=True))
    updater.dispatcher.add_handler(CommandHandler('stop', stop_timer, pass_job_queue=True))
    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()