from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo
from token_tg import BOT_TOKEN


dp = Dispatcher(BOT_TOKEN)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://antonilinskiy.github.io/tg_bot/')))
    await message.answer('Привет мой друг!', reply_markup=markup)

executor.start_polling(dp)

