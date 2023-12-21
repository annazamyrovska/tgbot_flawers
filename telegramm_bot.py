import telebot
import webbrowser
import sqlite3
from telebot import types

bot = telebot.TeleBot('6387289450:AAHtrw5QYWDqWDTCjolrq4FoxeANlBOTjCw')

name = None


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('itconn.sql')
    cur = conn.cursor()

    cur.execute(
        'CREATE TABLE IF NOT EXISTS users (id int auto_increment primery key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(
        message.chat.id, 'Привет, сейчас мы тебя зарегестрируем! Введи своё имя...')
    bot.register_next_step_handler(message, user_name)


def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)


def user_pass(message):
    password = message.text.strip()

    conn = sqlite3.connect('itconn.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users(name, pass) VALUES (?, ?)',
                (name, password))
    conn.commit()
    cur.close()
    conn.close()
    bot.send_message(
        message.chat.id, 'Привет, сейчас мы тебя зарегестрируем! Введи своё имя...')
    bot.register_next_step_handler(message, user_name)
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        'Список пользователей', callback_data='users'))
    bot.send_message(
        message.chat.id, 'Пользователь зарегестрирован', reply_markup=markup)
    # bot.register_next_step_handler(message, user_pass)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    site_up = types.KeyboardButton('Go to website')
    markup.row(site_up)
    site1 = types.KeyboardButton('Delete')
    site2 = types.KeyboardButton('Edit')
    markup.row(site1, site2)
    file = open('./649odjtkpzt61.png', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Hi', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)


def on_click(message):
    if message.text == 'Go to website':
        bot.send_message(message.chat.id, 'Website is open')
    elif message.text == 'Delete':
        bot.send_message(message.chat.id, 'Delete')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://jolse.com/index.html')


@bot.message_handler(content_types=['photo', 'audio'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    site_up = types.InlineKeyboardButton(
        'Go to website', url='https://www.google.com/')
    markup.row(site_up)
    site1 = types.InlineKeyboardButton('Delete', callback_data='delete')
    site2 = types.InlineKeyboardButton('Edit', callback_data='edit')
    markup.row(site1, site2)
    bot.reply_to(message, 'Wow', reply_markup=markup)


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id,
                           callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text(
            'Edit text', callback.message.chat.id, callback.message.message_id)


@bot.message_handler(commands=['start', 'hello', 'hi'])
def main(message):
    bot.send_message(message.chat.id, f'Hello {message.from_user.first_name}')


@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, 'Help information')


@bot.message_handler()
def info(message):
    if message.text.lower() == 'hi':
        bot.send_message(message.chat.id, f'Hello {
                         message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')


bot.polling(none_stop=True)
