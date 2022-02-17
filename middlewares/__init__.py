from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .big_brother import BigBrother
from .sentinel import Sentinel
from .acl import ACLMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(ACLMiddleware())
    dp.middleware.setup(Sentinel())
    dp.middleware.setup(BigBrother())
