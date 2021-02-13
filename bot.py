import telebot
import random

from telebot import types
bot = telebot.TeleBot('1611783065:AAG0ju470CF9FQ2WxW9Vr_NOX6QqQ4I9Nc0')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Ласкаво просимо!")
    bot.send_message(message.chat.id, "Чим можу допомогти?")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Що ти можеш?")
    item2 = types.KeyboardButton("Мені потрібна допомога")

    markup.add(item1, item2)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Привет':
        bot.send_message(message.chat.id, 'Привет!')
    elif message.text == 'Пока':
        bot.send_message(message.chat.id, "До новых встреч!")

bot.polling(none_stop=True)
