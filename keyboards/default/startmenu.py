from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


adtype_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Продам'), KeyboardButton(text='Куплю')],
        [KeyboardButton(text='Услуга'),KeyboardButton(text='Ищу Услугу')]],
    resize_keyboard=True
)

city_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Москва'), KeyboardButton(text='Санкт Петербург')],
        [KeyboardButton(text='Волгоград'), KeyboardButton(text='Воронеж'), KeyboardButton(text='Екатеринбург')],
        [KeyboardButton(text='Казань'), KeyboardButton(text='Красноярск'), KeyboardButton(text='ижний Новгород')],
        [KeyboardButton(text='Новосибирск'), KeyboardButton(text='Самара'), KeyboardButton(text='Уфа')]],
    resize_keyboard=True
)

yesno_buttons = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Да'), KeyboardButton(text='Нет')]],
    resize_keyboard=True
)

photo_button = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Достаточно фото, пошли дальше')]],
    resize_keyboard=True
)


startmenu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='О боте'),
            KeyboardButton(text='Правила')
        ],
        [
            KeyboardButton(text='Написать объявление')
        ],
    ],
    resize_keyboard=True
)

