from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

startmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="О боте"),
            KeyboardButton(text="Правила")
        ],
        [
            KeyboardButton(text="Написать объявление")
        ],
    ],
    resize_keyboard=True
)
