# Importações
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
from telegram import ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup, Update
import logging
#####################################################################################################################
# Outras coisas
p76ers = '\N{boxing glove} 76ers'
blazers = '🕒 Blazers'
bulls = '\N{cow face} Bulls'
bucks = ' 🇬🇷 Bucks'
cavs = '💘 Cavs'
celtics = '👴🏿 Celtics'
clippers = '🦞 Clippers'
grizzlies = '🐻 Grizzlies'
hawks = '🥶 Hawks'
heat = '\N{fire} Heat'
hornets = '🏀 Hornets'
jazz = '\N{spider} Jazz'
kings = '\N{crown} Kings'
knicks = '🌹 Knicks'
lakers = '🤴🏿 Lakers'
magic = '🎩 Magic'
mavericks = '👱🏻‍♂️ Mavs'
nets = '1️⃣3️⃣ Nets'
nuggets = '🃏 Nuggets'
pacers = '🅿️ Pacers'
pistons = '🔝 Pistons'
pelicans = '🌱 Pelicans'
raptors = '🦎 Raptors'
rockets = '🚀 Rockets'
suns = '\N{sun with face} Suns'
spurs = '🧽 Spurs'
timberwolves = '🐺 Wolves'
thunder = '⛈️ OKC'
warriors = '💦 Warriors'
wizards = '🧙‍♀️ Wizards'
#####################################################################################################################
# Bot

# Inicialização do Bot
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Iniciando o Bot
updater = Updater(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE', use_context=True)
dispatcher = updater.dispatcher

# Menu de operações ##################################################################################################
# Criando o menu de opções de operação, onde o usuário pode escolher entre WinWin ou Sniper
def menuOperacoes(update, context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(text=mensagemOperacoes(), reply_markup=menuOperacoesTeclado())

# Criando o teclado para o menu de operações
def menuOperacoesTeclado():
  operacoes = [[InlineKeyboardButton('🤑 Win Win', callback_data='winwin')],
               [InlineKeyboardButton('🎯 Sniper', callback_data='sniper')]]
  return InlineKeyboardMarkup(operacoes, one_time_keyboard=True)

# Mensagem de retorno para a escolha de time
def mensagemOperacoes():
    return 'Qual operação você deseja fazer?'

# Menu de Times #####################################################################################################
def menuTimes(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text='', reply_markup=Repl())
    query.edit_message_text(text=mensagemTimes(), reply_markup=menuTimesTeclado())

# Criando o teclado para o menu de operações
def menuTimesTeclado():
  times = [
            [blazers, p76ers],
            [clippers, bulls],
            [grizzlies, bucks],
            [jazz, cavs],
            [kings, celtics],
            [lakers, hawks],
            [mavericks, heat],
            [nuggets, hornets],
            [pelicans, knicks],
            [rockets, magic],
            [suns, nets],
            [spurs, pacers],
            [timberwolves, pistons],
            [thunder, raptors],
            [warriors, wizards],
        ]
  return ReplyKeyboardMarkup(times, one_time_keyboard=True)

# Mensagem de retorno para a escolha de time
def mensagemTimes():
    return 'Qual time deseja pesquisar?'

updater.dispatcher.add_handler(CallbackQueryHandler(menuTimes, pattern='winwin'))

# Comandos principais ###############################################################################################
# Criando a função para o comando /start
def start(update, context):
  update.message.reply_text(mensagemOperacoes(), reply_markup=menuOperacoesTeclado())

# Atrelando o /start à função Start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Definindo a função Unknown, que retorna uma mensagem para comandos desconhecidos
def comandoDesconhecido(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, não entendi o comando!")

# Adicionando o handler para mensagens desconhecidas
unknown_handler = MessageHandler(Filters.command, comandoDesconhecido)
dispatcher.add_handler(unknown_handler)

# Iniciando o Bot
updater.start_polling()

## Encerrando o Bot
# updater.stop()

