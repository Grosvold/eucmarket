import logging

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data

class IsPrivate(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        data = ctx_data.get()
        logging.info(f"4. Filter, {data=}")
        logging.info("Следующая точка: Process Message")
        return message.chat.type == types.ChatType.PRIVATE
