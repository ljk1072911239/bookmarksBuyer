# Iniciando o Bot
from telegram.ext import Updater
from telegram.ext.filters import Filters
from telegram import ReplyKeyboardMarkup
updater = Updater(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE', use_context=True)
dispatcher = updater.dispatcher

teclado2 = [
    ['1 - \N{grinning face with smiling eyes}'],
    ['2 - \N{face with tears of joy}']
    ]
menu = ReplyKeyboardMarkup(
    keyboard=teclado2,
    resize_keyboard=True,
    one_time_keyboard=True
)


# Função de login do bot
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Criando a função para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o Beto! Estou aqui pra te ajudar nas apostas esportivas!", reply_markup=menu)

# Atrelando o /start à função Start
from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start, Filters.user(user_id=1375793777))
dispatcher.add_handler(start_handler)

# Criando a função de mensagem winWin
from telegram.ext import MessageHandler
def winWin(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WinWin")

winwinHandler = MessageHandler(Filters.user(user_id=1375793777), winWin, '1 - \N{grinning face with smiling eyes}')

# Iniciando o Bot
updater.start_polling()