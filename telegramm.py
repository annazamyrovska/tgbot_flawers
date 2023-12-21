import telebot
import webbrowser
import sqlite3
from telebot import types

bot = telebot.TeleBot('6387289450:AAHtrw5QYWDqWDTCjolrq4FoxeANlBOTjCw')

name = None



@bot.message_handler(func=lambda message: message.text.lower() in ['hi', 'привет', 'hello'])
def handle_greeting(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Открыть магазин', url='https://github.com/annazamyrovska/tgbot_flawers.git/flowers.html'))
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}', reply_markup=markup)  
# @bot.message_handler(func=lambda message: True)
# def info(message):
#     markup = types.ReplyKeyboardMarkup()
#     markup.add(types.KeyboardButton('Открыть магазин', url='Python/flowers.html'))
#     bot.send_message(message.chat.id, 'Привет', reply_markup=markup)





bot.polling(none_stop=True)