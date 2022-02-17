from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.models import User
from utils.misc.sentinel import allow_access


@allow_access()
@dp.message_handler(Command("block_me"))
async def block_me(message: types.Message, user: User):
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ запрещен. "
                         f"Разблокировать можно по команде /unblock_me")
    user.block()


@allow_access()
@dp.message_handler(Command("unblock_me"))
async def block_me(message: types.Message, user: User):
    await message.answer(f"Пользователь имеет статус: {user.allowed}. Теперь доступ разрешен. "
                         f"Заблокировать можно по команде /block_me")
    user.allow()
