import logging

from typing import Union

from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery

from data.config import channel_name, ADMINS
from keyboards.inline.callback_datas import buy_callback
from keyboards.inline.choice_buttons import choice, about, onwheel_keyboard, apples_keyboard
from loader import dp


@dp.message_handler(Command("items"))
async def show_items(message: Message):
    await message.answer(text=f'Привет {message.from_user.first_name}! \nЯ бот для {channel_name}.\n'
                              f'Предлагаю ознакомиться с правилами и подать объявление.\n\n',
                           reply_markup=choice)


# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
@dp.callback_query_handler(text_contains="onwheel")
async def buying_onwheel(message: Union[Message, CallbackQuery]):
    if isinstance(message, Message):
        await message.answer(text=f'Привет', reply_markup=choice)
    elif isinstance(message, CallbackQuery):
        call = message

    #
    # # Обязательно сразу сделать answer, чтобы убрать "часики" после нажатия на кнопку.
    # # Укажем cache_time, чтобы бот не получал какое-то время апдейты, тогда нижний код не будет выполняться.
    # # await call.answer(cache_time=60)
    #     callback_data = call.data
    #
    # # Отобразим что у нас лежит в callback_data
    # # logging.info(f"callback_data='{callback_data}'")
    # # В питоне 3.8 можно так
    #     logging.info(f"{callback_data=}")

        await call.message.edit_text(f'Привет {call.message.from_user.first_name}! \nЯ бот для {channel_name}. Версия 0.8.0\n'
                              f'Создан @grosvold для EUC сообщества.\n'
                              f'Порядок на барахолке поддерживается этим ботом, и 15 модераторами.',
                              reply_markup=choice)


@dp.callback_query_handler(text_contains="back")
async def buying_onwheel(message: CallbackQuery):
    call = message
    await call.message.edit_text(text=f'Привет {message.from_user.first_name}! \nЯ бот для {channel_name}.\n'
                                      f'Предлагаю ознакомиться с правилами и подать объявление.\n\n',
                                 reply_markup=choice)


@dp.callback_query_handler(text_contains="opps")
async def opps(message: CallbackQuery):
    call = message
    await call.message.edit_text(text=
                                 f'На текущий момент бот умеет:\n'
                                 f'+ Базовое меню\n'
                                 f'\nВ разработке:\n'
                                 f'- последовательным заполнением публиковать объявление в канале {str(config.channel_name)}\n'
                                 f'- опрашивает на необходимые хештеги, цену\n'
                                 f'- поддерживает до 4 фото\n'
                                 f'- указывает ссылку на автора объявления\n'
                                 f'- встроен фильтр матерных слов\n'
                                 f'- удаление объявлений\n'
                                 f'- уведомления о комментариях\n'
                                 f'- разделение на категории'
                                 f'\nВ перспективе:\n'
                                 f'- исправление изменений\n'
                                 f'- отзывы и рейтинг\n'
                                 f'- прогрессивная система блокировки для нарушителей правил',
                                 reply_markup=about)


# Попробуйем отловить по встроенному фильтру, где в нашем call.data содержится "pear"
@dp.callback_query_handler(text_contains="about")
async def about(message: Union[Message, CallbackQuery]):
    if isinstance(message, Message):
        await message.answer(text=f'Привет', reply_markup=choice)
    elif isinstance(message, CallbackQuery):
        call = message

        await call.message.edit_text(f'Привет {call.message.from_user.first_name}! \nЯ бот для {channel_name}. Версия 0.8.0\n'
                              f'Создан @grosvold для EUC сообщества.\n'
                              f'Порядок на барахолке поддерживается этим ботом, и 15 модераторами.',
                              reply_markup=about)


# Попробуем использовать фильтр от CallbackData
@dp.callback_query_handler(buy_callback.filter(item_name="apple"))
async def buying_apples(call: CallbackQuery, callback_data: dict):
    await call.answer(cache_time=60)

    # Выведем callback_data и тут, чтобы сравнить с предыдущим вариантом.
    logging.info(f"{callback_data=}")

    quantity = callback_data.get("quantity")
    await call.message.answer(f"Вы выбрали купить яблоки. Яблок всего {quantity}. Спасибо.",
                              reply_markup=apples_keyboard)


@dp.callback_query_handler(text="cancel")
async def cancel_buying(call: CallbackQuery):
    # Ответим в окошке с уведомлением!
    await call.answer("Вы нажали Отмена!")#, show_alert=True)

    # Вариант 1 - Отправляем пустую клваиатуру изменяя сообщение, для того, чтобы ее убрать из сообщения!
    await call.message.edit_reply_markup(reply_markup=None)

    # Вариант 2 отправки клавиатуры (по API)
    # await bot.edit_message_reply_markup(chat_id=call.from_user.id,
    #                                     message_id=call.message.message_id,
    #                                     reply_markup=None)
