import re

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from data.config import channel_name, ADMINS
from loader import dp

@dp.message_handler(IsPrivate(), user_id=ADMINS, text="/start")
async def admin_chat_secret(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! ! \nЯ бот для {channel_name}.\n"
                         f"Ты в списке модераторов, цели модератора здесь: https://t.me/c/1163833793/2 \n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")


@dp.message_handler(CommandStart(deep_link=re.compile(r"\d\d\d")))
async def bot_start(message: types.Message):
    deep_links_args = message.get_args()
    await message.answer(f"Привет, {message.from_user.full_name}! ! \nЯ бот для {channel_name}.\n"
                         f"Ты пришел по приглашению {deep_links_args}\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! ! \nЯ бот для {channel_name}.\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление.")

