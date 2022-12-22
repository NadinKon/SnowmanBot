from  aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove

#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать! Я бот-снеговик Маруся!', reply_markup=kb_client)
    await message.delete()

#@dp.message_handler(commands=['Режим_работы'])
async def open_command(message : types.Message):
    await bot.send_message(message.from_user.id, '1/364 дня')

#@dp.message_handler(commands=['Адрес'])
async def place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Северный полюс')

# @dp.message_handler(commands=['Меню'])
# async def menu_command(message : types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

def register_handler_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(open_command, commands=['Режим_работы'])
    dp.register_message_handler(place_command, commands=['Адрес'])