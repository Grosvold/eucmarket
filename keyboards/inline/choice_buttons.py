from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback

about_button = InlineKeyboardButton(text="О боте", callback_data="about")
rules_button = InlineKeyboardButton(text="Правила", url="https://t.me/EUC_market_RU/3")
cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
newad_button = InlineKeyboardButton(text="Написать объявление", callback_data="newad")
back_button = InlineKeyboardButton(text="В начало", callback_data="back")
school_button = InlineKeyboardButton(text="Купи тут", url="https://onwheel.com")
opps_button = InlineKeyboardButton(text="Возможности", callback_data="opps")
helpus_button = InlineKeyboardButton(text="Помочь проекту", callback_data="helpus")

# Вариант 1, как в прошлом уроке
choice = InlineKeyboardMarkup(inline_keyboard=[
    [
        about_button, rules_button
    ],
    [
        newad_button
    ],
    [
        cancel_button
    ]
])


# Вариант 2 - с помощью row_width и insert.
about = InlineKeyboardMarkup(inline_keyboard=[
    [
        about_button, opps_button
    ],
    [
        helpus_button
    ],
    [
        newad_button, rules_button
    ],
    [
        back_button, cancel_button
    ]
])

#
# choice = InlineKeyboardMarkup(row_width=2)
#
# buy_onwheel = InlineKeyboardButton(text="О боте", callback_data=buy_callback.new(item_name="onwheel", quantity=1))
# choice.insert(buy_onwheel)
#
# buy_rules = InlineKeyboardButton(text="Правила", url="https://t.me/EUC_market_RU/3")
# choice.insert(buy_rules)
#
# new_ad = InlineKeyboardButton(text="Написать объявление", callback_data="newad")
# choice.insert(new_ad)
#
# back_button = InlineKeyboardButton(text="Назад", callback_data="back")
# choice.insert(back_button)
#
# cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
# choice.insert(cancel_button)


# А теперь клавиатуры со ссылками
rules_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        rules_button
    ]
])

onwheel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        school_button
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        rules_button
    ]
])