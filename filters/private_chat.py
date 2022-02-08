from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsPrivaye(BoundFilter):
    async def check(self, message: types.message) -> bool:
        return message.text = "/start"