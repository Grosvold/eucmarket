from aiogram import Dispatcher

from filters.test_filter import SomeF
from .private_chat import IsPrivate
from loader import dp
# from .is_admin import AdminFilter


if __name__ == "filters":
    # dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(IsPrivate)
    pass
