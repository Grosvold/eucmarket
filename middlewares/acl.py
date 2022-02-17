# Modified example from https://github.com/aiogram/bot/blob/master/app/middlewares/acl.py
# Access Control List

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

from utils.db_api.models import User


class ACLMiddleware(BaseMiddleware):
    def setup_chat(self, data: dict, user: types.User):
        user_id = user.id

        # user = User.get(user_id)
        # user = await User.get() - for ORM or         # user = await quick_commands.select_user()
        # if user is None:
        #     user = User.create(telegram_id=user_id)
        user = User.get_or_create(user_id)
        data["user"] = user

    async def on_pre_process_message(self, message: types.Message, data: dict):
        self.setup_chat(data, message.from_user)

    async def on_pre_process_callback_query(self, query: types.CallbackQuery, data: dict):
        self.setup_chat(data, query.from_user)
