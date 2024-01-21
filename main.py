import telebot
import os
from googletrans import Translator
from langdetect import detect
from dotenv import load_dotenv
from telebot import types

load_dotenv()
TOKEN = os.environ['TOKENAPI']
bot = telebot.TeleBot(TOKEN, parse_mode=None)


bot.set_webhook()

translator = Translator()
@bot.message_handler(commands=['start'])
def start(message):
    markup =types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1=types. KeyboardButton('/help')
    btn2=types. KeyboardButton('история переводов')

    markup.add(btn1,btn2)

    bot.send_message(message.chat.id,text="привет это бот переводчик , он переводит любые слова и словосочетания всех языков  мира на русский!",reply_markup=markup)


@bot.message_handler(func=lambda m: True)
def translate_message(message):
    if (message.text == "/start"):
        bot.send_message(message.chat.id,text="привет это бот переводчик , он переводит любые слова и словосочетания всех языков  мира на русский!")
    elif (message.text == "/help"):
        bot.send_message(message.chat.id,text="отправьте боту сообщение на любом языке мира и он переведёт их на русский!")
    elif (message.text == "история переводов"):
        bot.send_message(message.chat.id,text="эта функция не работает")
    else:
        src = detect(message.text)
        dest = 'ru'
        translated_text = translator.translate(message.text, src=src, dest=dest).text
        bot.send_message(message.chat.id, translated_text)


bot.polling(none_stop=True)
