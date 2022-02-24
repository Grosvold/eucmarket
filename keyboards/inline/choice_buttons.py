from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback

# Вариант 1, как в прошлом уроке
about = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="О боте", callback_data="about"),
        InlineKeyboardButton(text="Правила", url="https://t.me/EUC_market_RU/3")
    ],
    [
        InlineKeyboardButton(text="Отмена", callback_data="cancel")
    ]
])


# Вариант 2 - с помощью row_width и insert.
choice = InlineKeyboardMarkup(row_width=2)

buy_onwheel = InlineKeyboardButton(text="О боте", callback_data=buy_callback.new(item_name="onwheel", quantity=1))
choice.insert(buy_onwheel)

buy_rules = InlineKeyboardButton(text="Правила", url="https://t.me/EUC_market_RU/3")
choice.insert(buy_rules)
#
# buy_apples = InlineKeyboardButton(text="Правила", callback_data="buy:apple:5")
# choice.insert(buy_apples)

new_ad = InlineKeyboardButton(text="Написать объявление", callback_data="newad")
choice.insert(new_ad)

back_button = InlineKeyboardButton(text="Назад", callback_data="back")
choice.insert(back_button)

cancel_button = InlineKeyboardButton(text="Отмена", callback_data="cancel")
choice.insert(cancel_button)

#
# about = InlineKeyboardMarkup(row_width=2)
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


# А теперь клавиатуры со ссылками на товары
rules_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Правила  тут", url="https://t.me/EUC_market_RU/3")
    ]
])

onwheel_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Купи тут", url="https://onwheel.com")
    ]
])

apples_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Правила  тут", url="https://t.me/EUC_market_RU/3")
    ]
])