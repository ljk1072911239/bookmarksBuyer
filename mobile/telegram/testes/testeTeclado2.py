from telegram import ReplyKeyboardMarkup

teclado2 = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
         ['0'],
]

teclado = [
    ['BUCETA'],
    ['2 - \N{face with tears of joy}']
    ]

menu = ReplyKeyboardMarkup(
    keyboard=teclado2,
    resize_keyboard=True,
    one_time_keyboard=True
)


# Iniciando o Bot
from telegram.ext import Updater
updater = Updater(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE', use_context=True)
dispatcher = updater.dispatcher


# Função de login do bot
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Criando a função para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o Beto! Estou aqui pra te ajudar nas apostas esportivas!", reply_markup=menu)

# Atrelando o /start à função Start
from telegram.ext import CommandHandler,MessageHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)



def testeRegex(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="BUCETAO")

from telegram.ext import Filters
buceta_handler = MessageHandler(Filters.regex(r'BUCETA'), testeRegex)
dispatcher.add_handler(buceta_handler)


# Iniciando o Bot
updater.start_polling()