from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from filters import IsPrivate
from data.config import channel_name, ADMINS
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}! ! \nЯ бот для {channel_name}.\n"
                         f"Предлагаю ознакомиться с правилами и подать объявление."
        # reply_markup=ReplyKeyboardMarkup(reply_keyboard, resize_keyboard=True, one_time_keyboard=False),
    )

