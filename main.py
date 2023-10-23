import telebot
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ['TOKEN']
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")





@bot.message_handler(func=lambda m: True)



def echo_all(message):
	markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
	but1 = telebot.types.KeyboardButton('перевод в png')
	but2 = telebot.types.KeyboardButton('перевод в jpg')
	markup.add(but1, but2)
	if message.text =='перевод в png':
		bot.send_message(message.chat.id, "добавьте файл в формате Jpg", reply_markup=markup)
		import aspose.words as aw
		doc = aw.Document()
		builder = aw.DocumentBuilder(doc)
		shape = builder.insert_image("Input.jpg")
		shape.image_data.save("Output.png")
	elif message.text == 'перевод в jpg':
		bot.send_message(message.chat.id, "добавьте файл в формате Png", reply_markup=markup)
		import aspose.words as aw
		doc = aw.Document()
		builder = aw.DocumentBuilder(doc)
		shape = builder.insert_image("Input.png")
		shape.image_data.save("Output.jpg")
	else:
		bot.send_message(message.chat.id, "файл не в нужном формате" + "!", reply_markup=markup)


bot.infinity_polling()
