import re
import logging

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from data.config import channel_name, ADMINS
from loader import dp, bot

# Проверка реферальной (пригласительной) ссылки
@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start(message: types.Message):
    deep_links_args = message.get_args()
    bot_user = await dp.bot.me
    deep_link = f"https://t.me/{bot_user.username}?start=12345"
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n"
                         f"{deep_links_args} передаёт тебе привет!\n"
                         f"Твоя диплинк ссылка - {deep_link}\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")


# Специальное приветствие для админов
@dp.message_handler(IsPrivate(), user_id=ADMINS, text="/start")
async def admin_chat_secret(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n"
                         f"Ты в списке модераторов, цели модератора здесь: https://t.me/c/1163833793/2 \n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")


# Стандартное приветствие в личку
@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! \nЯ бот для {channel_name}.\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")


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
