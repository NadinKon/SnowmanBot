import string

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import os, json

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
    print("Готов работать")

"""***клиентская часть"""
@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, 'Добро пожаловать! Я бот-снеговик Маруся!')
    await message.delete()

@dp.message_handler(commands=['Режим_работы'])
async def open_command(message : types.Message):
    await bot.send_message(message.from_user.id, '1/364 дня')

@dp.message_handler(commands=['Адрес'])
async def place_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Северный полюс')

# @dp.message_handler(commands=['Меню'])
# async def menu_command(message : types.Message):
#     for ret in cur.execute('SELECT * FROM menu').fetchall():
#         await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена {ret[-1]}')

'''***адм.часть'''


'''*Общая часть'''



@dp.message_handler()
async def echo(message : types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))) != set():
        await message.reply("Не ругаться")
        await message.delete()



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
