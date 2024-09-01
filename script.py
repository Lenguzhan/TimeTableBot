import telebot

import webbrowser
import pyscreenshot
import time


bot = telebot.TeleBot('7262655282:AAE6nZxYjeeluwo7nv4A6SSgv_OvGkXA0jI')

@bot.message_handler(commands=['расписание'])
def start(message):
    webbrowser.open('https://goo.su/1ZY7')
    time.sleep(5)
    screen = pyscreenshot.grab(bbox=(0, 88, 1740, 1000))
    screen.save('screen1.png')
    bot.send_photo(message.chat.id, screen)

bot.polling(none_stop=True)

