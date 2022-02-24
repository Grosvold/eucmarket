import re
import logging

from aiogram import types
from aiogram.dispatcher.filters import Command, CommandStart
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from filters import IsPrivate, SomeF
from data.config import channel_name, ADMINS
from loader import dp, bot
from utils.db_api.models import User
from keyboards.inline.choice_buttons import choice
from utils.misc import rate_limit


# Проверка реферальной (пригласительной) ссылки
@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start(message: types.Message, middleware_data):
    deep_links_args = message.get_args()
    bot_user = await dp.bot.me
    deep_link = f"https://t.me/{bot_user.username}?start=Grosvold"
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n"
                         f"{deep_links_args} передаёт тебе привет!\n"
                         f"Твоя диплинк ссылка - {deep_link}\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.\n"
                         f"{middleware_data=}")


# Специальное приветствие для админов
@dp.message_handler(IsPrivate(), user_id=ADMINS, text="/start")
async def admin_chat_secret(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n"
                         f"Ты в списке модераторов, цели модератора здесь: https://t.me/c/1163833793/2 \n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.",
                         reply_markup=choice)


# Стандартное приветствие в личку
# @rate_limit(5, key="start")
@dp.message_handler(IsPrivate(), Command("star"), SomeF())
async def bot_start(message: types.Message, middleware_data, from_filter, user: User):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n" 
                         #f"{middleware_data=} \n{from_filter=}\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.",
                         reply_markup=choice)
    logging.info(f"6. Handler")
    logging.info("Следующая точка: Post Process Message")
    return {"from_handler": "Данные из хендлера"}


@dp.callback_query_handler(text="button")
async def get_button(call: types.CallbackQuery):
    await call.message.answer("Вы нажали на кнопку")


# ==================
# @dp.message_handler(CommandStart())
# async def bot_start(message: types.Message):
#     non_existing_user = 666666
#
#     # Не попадает в эррор хендер, обрабатывается тут с помощью try
#     try:
#         await message.answer("Неправильно закрыт <b>тег<b>")
#     except Exception as err:
#         await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")
#
#     # Не попадает в эррор хендер
#     try:
#         await bot.send_message(chat_id=non_existing_user, text="Не существующий пользователь")
#     except Exception as err:
#         await message.answer(f"Не попало в эррор хендлер. Ошибка: {err}")
#
#     # Попадает отсюда в эррор хендлер
#     await message.answer("Не существует <kek>тега</kek>")
#     logging.info("Это не выполнится, но бот не упадет.")
#
#     # Все что ниже - не выполнится, но бот не упадет
#
#     await message.answer("...")
# =================
