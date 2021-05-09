from sys import exc_info as error
from urllib.request import urlopen
from urllib.parse import urlencode
import json

TOKEN = '1617028046:AAGjLJ4keMN2uz3GFUxQ3NYnJwLyLFtsegI'
URL = f'https://api.telegram.org/bot{TOKEN}'
STATUS = True
OFFSET = 0

def call_api_method(method='getMe', data=None):
  # Call API method with data.
  data = urlencode(data).encode("utf-8") if data else data
  response = urlopen(f'{URL, method}/{data}')
  return json.loads(response.read())

def get_me():
  # Get bot info.
  bot = call_api_method()
  return type('Bot', (), dict(bot['result']))

def get_updates():
  # Get new updates from Telegram.
  data = {'offset': OFFSET, 'limit': 0, 'timeout': 0}
  return type('Updates', (), call_api_method('getUpdates', data))

def handle(update):
  # Make usefull objects.
  message = type('Message', (object,), dict(update['message']))
  user = type('User', (), dict(update['message']['from']))
  chat = type('Chat', (), dict(update['message']['chat']))
  return message, user, chat

def send_message(chat_id, message):
  # Send message to specific chat.
  data = {'text': message,
          'chat_id': chat_id,
          'parse_mode': 'Markdown',
          'disable_web_page_preview': True}
  call_api_method('sendMessage', data)


def send_keyboard(chat_id, message, keyboard):
  # Send message and keyboard to specific chat.
  data = {'text': message,
          'chat_id': chat_id,
          'parse_mode': 'Markdown',
          'reply_markup': reply_markup(keyboard),
          'disable_web_page_preview': 'true'}
  call_api_method('sendMessage', data)

def reply_markup(keyboard):
  # Serialize keyboard data to JSON.
  return json.dumps({'keyboard': keyboard,
                     'resize_keyboard': True,
                     'one_time_keyboard': True,
                     'selective': True})

def main_keyboard():
  # Main menu.
  return [first_button(), second_button()]

def one_line_keyboard():
  # Menu with buttons in one line.
  return [two_buttons()]

def first_button():
  # Single keyboard button.
  return ['first button']

def second_button():
  # Single keyboard button.
  return ['second button']

def two_buttons():
  # Two buttons on one line.
  return ['left button', 'right button']


while STATUS:
  # Get updates forever. Except if get Error.
  try:
    if not OFFSET:
      OFFSET = 1
      # Print bot info on the start.
      bot = get_me()
      print(f'Bot @{bot.username} is running...')

    updates = get_updates()

    for update in updates.result:
      # Handle last update.
      OFFSET = update['update_id'] + 1
      message, user, chat = handle(update)

      # Greeting user by full name.
      greeting = f'Hello, {user.first_name} {user.last_name}!'

      #send_message(chat.id, greeting)
      send_keyboard(chat.id, greeting, one_line_keyboard())
  except:
    STATUS = False
    print('\nERROR:\t', error()[1])
