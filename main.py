import telebot
import os
from googletrans import Translator
from langdetect import detect
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN, parse_mode=None)


bot.set_webhook()

translator = Translator()

@bot.message_handler(func=lambda m: True)


def translate_message(message):
  src = detect(message.text)
  dest = 'ru'
  translated_text = translator.translate(message.text, src=src, dest=dest).text
  bot.send_message(message.chat.id, translated_text)
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(перевод не верный)
    markup.add(button1)


def func(message):
  if (message.text == ""):


bot.polling()
