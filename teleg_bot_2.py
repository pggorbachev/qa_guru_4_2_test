import telebot
from telebot import types

bot = telebot.TeleBot('6160440363:AAEyDIbyPsJz4U7Jd0NMLri4mLwdBLdbXYY')


@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardButton(row_width=2)
    for_boy = types.InlineKeyboardButton('Я парень', callback_data='boy')
    for_girl = types.InlineKeyboardButton('Я девушка', callback_data='girl')
    markup.add(for_boy, for_girl)
    bot.send_message(message.chat.id, "Hello!", reply_markup=markup)

if __name__ == '__main__':
    bot.polling(none_stop=True)
