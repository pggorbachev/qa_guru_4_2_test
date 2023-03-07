import telebot

bot = telebot.TeleBot('6160440363:AAEyDIbyPsJz4U7Jd0NMLri4mLwdBLdbXYY')


@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    boy_button = telebot.types.KeyboardButton('Boy')
    girl_button = telebot.types.KeyboardButton('Girl')
    markup.add(boy_button, girl_button)
    bot.send_message(message.chat.id, 'Выберите пол:', reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == 'Girl')
def girl_handler(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)
    coffee_button = telebot.types.KeyboardButton('Сделать кофе')
    tea_button = telebot.types.KeyboardButton('Сделать чай')
    shop_button = telebot.types.KeyboardButton('Сходить в магазин')
    champagne_button = telebot.types.KeyboardButton('Подать шампанское')
    massage_button = telebot.types.KeyboardButton('Помассировать плечи')
    markup.add(coffee_button, tea_button, shop_button, champagne_button, massage_button)
    bot.send_message(message.chat.id, 'Выберите задание для boy:', reply_markup=markup)


@bot.message_handler(
    func=lambda message: message.text in ['Сделать кофе', 'Сделать чай', 'Сходить в магазин', 'Подать шампанское',
                                          'Помассировать плечи'])
def task_handler(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} выбрала задание "{message.text}" для boy')


if __name__ == '__main__':
    bot.polling(none_stop=True)
