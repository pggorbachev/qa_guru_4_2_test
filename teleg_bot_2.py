from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

bot = Bot('6115591165:AAEktXiWG7z59jDANksoRW1o9oDJspqiADI')
dp = Dispatcher(bot)


async def on_start(_):
    print('C 8 Марта!')


keybord = ReplyKeyboardMarkup(resize_keyboard=True)
button_girl = KeyboardButton(text='/girl')
button_boy = KeyboardButton(text='/boy')
keybord.add(button_boy, button_girl)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='startuem',
                           reply_markup=keybord)


@dp.message_handler(commands=['girl'])
async def girl_caprise(message: types.Message):
    caprises = InlineKeyboardMarkup(row_width=2)
    tea = InlineKeyboardButton(text='Сделать чаю',
                               callback_data='tea')
    coffe = InlineKeyboardButton(text="Сделать кофя",
                                 callback_data='coffe')
    goto_shop = InlineKeyboardButton(text='Сходи в магазин',
                                    callback_data='shop')
    shampain = InlineKeyboardButton(text='Подать шампанскага Царице',
                                     callback_data='shampain')
    shoulders = InlineKeyboardButton(text='Помассировать плечи',
                                   callback_data='shoulders')
    caprises.add(tea, coffe, goto_shop, shampain, shoulders)

    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://i4.stat01.com/2/5974/159738867/afacdb/buket-iz-raznocvetnoj-gipsofily.jpg',
                         reply_markup=caprises)


@dp.callback_query_handler()
async def feedback_do(callback: types.CallbackQuery):
    for caprise in callback.data:
        if caprise == 'tea':
            await callback.answer('Чай уже к вам едет')
            break
        elif caprise == 'coffe':
            await callback.answer('Кофе с берегов кении уже готовится')
            break
        elif caprise == 'shop':
            await callback.answer('im going')
            break
        elif caprise == 'shampain':
            await callback.answer('byxaem?')
            break
        elif caprise == 'shoulders':
            await callback.answer('masag')
    # if callback.data == 'give_tea':
    #     await callback.answer("Будет исполнено!")


if __name__ == "__main__":
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_start)