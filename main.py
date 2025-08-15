import telebot
import os
from googletrans import Translator
from langdetect import detect
from dotenv import load_dotenv
import sqlite3
import emoji
from telebot import types
from PIL import Image
import requests
from io import BytesIO

load_dotenv()
token = os.environ['tokenapi']
bot = telebot.TeleBot(token, parse_mode='HTML')
bot.set_webhook()
translator = Translator()


def extract_text_from_image(image_bytes):
    API_KEY = os.environ['sanyAPI'] 
    url = 'https://api.ocr.space/parse/image'

    response = requests.post(
        url,
        files={'image': ('image.jpg', image_bytes, 'image/jpeg')},
        data={'apikey': API_KEY, 'language': 'rus'}
    )

    result = response.json()

    if result.get('IsErroredOnProcessing', False):
        error_message = result.get('ErrorMessage', 'Unknown error occurred')
        raise Exception(f"OCR API error: {error_message}")

    if not result.get('ParsedResults'):
        raise Exception("No text found in the image")

    return result['ParsedResults'][0]['ParsedText']


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    conn = sqlite3.connect(f'{user_id}.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS c
                ( user_message TEXT, bot_message TEXT)''')
    conn.commit()
    conn.close()

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('/help')
    btn2 = types.KeyboardButton('история переводов')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,
                     text="Привет, это бот-переводчик! Он переводит текст с любых языков мира на русский. "
                          "Можно отправлять как текстовые сообщения, так и изображения с текстом.",
                     reply_markup=markup)


@bot.message_handler(content_types=['photo'])
def handle_image(message):
    try:
        user_id = message.from_user.id

        file_info = bot.get_file(message.photo[-1].file_id)
        file_url = f'https://api.telegram.org/file/bot{token}/{file_info.file_path}'

        response = requests.get(file_url)
        img_bytes = BytesIO(response.content)

        extracted_text = extract_text_from_image(img_bytes)

        if not extracted_text.strip():
            bot.reply_to(message, "Не удалось распознать текст на изображении.")
            return

        try:
            src_lang = detect(extracted_text)
        except:
            src_lang = 'en'

        translated_text = translator.translate(extracted_text, src=src_lang, dest='ru').text

        conn = sqlite3.connect(f'{user_id}.db')
        c = conn.cursor()
        c.execute("INSERT INTO c (user_message, bot_message) VALUES (?, ?)",
                  (extracted_text, translated_text))
        conn.commit()
        conn.close()

        bot.reply_to(message, f"Распознанный текст:\n{extracted_text}\n\nПеревод на русский:\n{translated_text}")

    except Exception as e:
        bot.reply_to(message, f"Произошла ошибка при обработке изображения: {str(e)}")


@bot.message_handler(func=lambda m: True)
def translate_message(message):
    user_id = message.from_user.id
    conn = sqlite3.connect(f'{user_id}.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS c
                ( user_message TEXT, bot_message TEXT)''')
    conn.commit()

    if message.text == "/start":
        start(message)
    elif ":" in emoji.demojize(message.text):
        bot.send_message(message.chat.id, text="Пожалуйста, введите текст без эмодзи")
    elif message.text == "/help":
        bot.send_message(message.chat.id,
                         text="Отправьте боту сообщение на любом языке мира, и он переведёт его на русский!\n"
                              "Также можно отправить изображение с текстом, и бот распознает и переведёт текст с картинки.")
    elif message.text.lower() == "история переводов":
        conn = sqlite3.connect(f'{user_id}.db')
        c = conn.cursor()
        c.execute("SELECT * FROM c")
        history = c.fetchall()
        conn.close()

        if not history:
            bot.send_message(message.chat.id, "История переводов пуста.")
            return

        result = 'История переводов:\n\n'
        for row in history:
            result += f"Исходный текст: {row[0]}\nПеревод: {row[1]}\n\n"

        if len(result) > 4000:
            for x in range(0, len(result), 4000):
                bot.send_message(message.chat.id, result[x:x + 4000])
        else:
            bot.send_message(message.chat.id, result)
    else:
        try:
            src_lang = detect(message.text)
            translated_text = translator.translate(message.text, src=src_lang, dest='ru').text

            conn = sqlite3.connect(f'{user_id}.db')
            c = conn.cursor()
            c.execute("INSERT INTO c (user_message, bot_message) VALUES (?, ?)",
                      (message.text, translated_text))
            conn.commit()
            conn.close()

            bot.send_message(message.chat.id, translated_text)
        except Exception as e:
            bot.send_message(message.chat.id, f"Произошла ошибка при переводе: {str(e)}")


if __name__ == '__main__':
    bot.polling(none_stop=True)
