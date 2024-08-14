from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('7357533859:AAGC3ouB_xHJDoRp6lRlMM5GPhbmDJ5HpEU')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://antonilinskiy.github.io/tg_bot/')))
    await message.answer('Привет мой друг!', reply_markup=markup)

executor.start_polling(dp)
