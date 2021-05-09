# Iniciando o Bot
from telegram.ext import Updater
updater = Updater(token='1620572588:AAGYxjvVCYXcDdAppUYknBESLhDt8luPcPE', use_context=True)
dispatcher = updater.dispatcher


# Função de login do bot
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Criando a função para o comando /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá, eu sou o Beto! Estou aqui pra te ajudar nas apostas esportivas!")

# Atrelando o /start à função Start
from telegram.ext import CommandHandler, RegexHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# Iniciando o Bot
updater.start_polling()

# Definindo a função Echo, que repete o que o usuário envia
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Atrelando qualquer mensagem que não seja um comando à função Echo
from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# Criando a função Caps, que retornaum texto escrito em caps
## Exemplo: /caps exemplo -> EXEMPLO
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

# Atrelando a função Caps para o comando /caps
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

## Criando funcionalidade inline para o Bot
# from telegram import InlineQueryResultArticle, InputTextMessageContent
# def inline_caps(update, context):
#     query = update.inline_query.query
#     if not query:
#         return
#     results = list()
#     results.append(
#         InlineQueryResultArticle(
#             id=query.upper(),
#             title='Caps',
#             input_message_content=InputTextMessageContent(query.upper())
#         )
#     )
#     context.bot.answer_inline_query(update.inline_query.id, results)
#
# from telegram.ext import InlineQueryHandler
# inline_caps_handler = InlineQueryHandler(inline_caps)
# dispatcher.add_handler(inline_caps_handler)


# Definindo a função Unknown, que retorna uma mensagem para comandos desconhecidos
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Desculpe, não entendi o comando!")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
dispatcher.add_handler(unknown_handler)
# updater.stop()
