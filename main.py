import telebot
import os
from googletrans import Translator
from langdetect import detect
from dotenv import load_dotenv
from telebot import types
import sqlite3

load_dotenv()
token = os.environ['tokenapi']
bot = telebot.TeleBot(token, parse_mode='HTML')
bot.set_webhook()
translator = Translator()

conn = sqlite3.connect('chat_history.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS chat_history
            (user_message TEXT, bot_message TEXT)''')
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('история переводов')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="привет это бот переводчик , он переводит любые слова и словосочетания всех языков мира на русский!", reply_markup=markup)

@bot.message_handler(func=lambda m: True)
def translate_message(message):
    if message.text == "/start":
        bot.send_message(message.chat.id, text="привет это бот переводчик , он переводит любые слова и словосочетания всех языков мира на русский!")
    elif message.text == "/help":
        bot.send_message(message.chat.id, text="отправьте боту сообщение на любом языке мира и он переведёт их на русский!")
    elif message.text == "история переводов":
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        c.execute("SELECT * FROM chat_history")
        chat_history = c.fetchall()
        conn.close()
        a=[]
        for row in chat_history:
            a.append(row)
        c='История переводов:\n\n'
        for i in a:
            c+=str(i[0])+' '+'-'+' '+str(i[1])
            c+=('\n')
        bot.send_message(message.chat.id,c)
    else:
        conn = sqlite3.connect('chat_history.db')
        src = detect(message.text)
        dest = 'ru'
        translated_text = translator.translate(message.text, src=src, dest=dest).text
        bot.send_message(message.chat.id, translated_text)
        conn = sqlite3.connect('chat_history.db')
        c = conn.cursor()
        c.execute("INSERT INTO chat_history (user_message, bot_message) VALUES (?, ?)", (message.text, translated_text))
        conn.commit()
        conn.close()

bot.polling(none_stop=True)
