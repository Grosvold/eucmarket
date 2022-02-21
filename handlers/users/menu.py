import logging

from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove

from data.config import channel_name, ADMINS
from keyboards.default import startmenu
from loader import dp


@dp.message_handler(Command("menu"))
async def show_menu(message: Message):
    await message.answer(
        f'Привет {message.from_user.first_name}! \nЯ бот для {channel_name}.\n'
        f'Предлагаю ознакомиться с правилами и подать объявление.\n\n',
    reply_markup=startmenu)

@dp.message_handler(text="О боте")
async def get_cotletki(message: Message):
    await message.answer(f"Вы выбрали {message.text}.")

@dp.message_handler(text="О боте")
async def get_cotletki(message: Message):
    await message.answer(f"Вы выбрали {message.text}.")

@dp.message_handler(Text(equals=["Правила", "Написать объявление"]))
async def get_food(message: Message):
    await message.answer(f"Вы выбрали {message.text}. Спасибо") # , reply_markup=ReplyKeyboardRemove())


