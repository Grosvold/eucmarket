from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import startmenu, adtype_buttons, city_buttons, yesno_buttons, photo_button
from keyboards.inline.choice_buttons import choice, about, onwheel_keyboard, apples_keyboard
from data.config import channel_name

from loader import dp
from states.test import AdvertQA


# Сделаем фильтр на комманду /test, где не будет указано никакого состояния
@dp.message_handler(Command("test"), state=None)
async def enter_test(message: types.Message):
    await message.answer('Давай заполним объявление.\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
        'Для начала определимся, какой тип объявления?')
    # Вариант 1 - с помощью функции сет
    await AdvertQA.Q1.set()
    # Вариант 2 - с помощью first
    # await AdvertQA.first() или ранее Test.first()



@dp.callback_query_handler(text_contains="newad")
async def get_button(call: types.CallbackQuery):
    await call.message.answer('Давай заполним объявление.\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
        'Для начала определимся, какой тип объявления?',
        reply_markup=adtype_buttons)
    await AdvertQA.Q1.set()


@dp.message_handler(state=AdvertQA.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
#
#     # Вариант 2 получения state
#     # state = dp.current_state(chat=message.chat.id, user=message.from_user.id)
#
#     # Вариант 1 сохранения переменных - записываем через key=var
#     # Если у вас запись идет какого-то параметра (например email) то записывайте не answer,
#     # а email, чтобы потом было понятно что именно доставать
#     await state.update_data(answer1=answer)
#
#     # Вариант 2 - передаем как словарь
    await state.update_data(
        {"answer1": answer}
    )
#
#     # Вариант 3 - через state.proxy
#     async with state.proxy() as data:
#         data["answer1"] = answer
#         # Удобно, если нужно сделать data["some_digit"] += 1
#         # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать
#
    await message.answer('В каком городе ты находишься? Выбери или напиши словом\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                         , reply_markup=city_buttons)
    await AdvertQA.next()
    # await Test.Q2.set()


@dp.message_handler(state=AdvertQA.Q2)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer2": answer}
    )
    await message.answer('Отлично! Возможен ли пересыл почтой или ТК?\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                         , reply_markup=yesno_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer3": answer}
    )
    await message.answer(
        'Фото пока не работают'
        'Супер. Приложи фото. Пока не больше четырёх.\n'
        'Можешь в одном альбоме. Можешь по одной.\n'
        'Или /skip если фото не нужно.\n\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
        , reply_markup=photo_button)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q4)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer4": answer}
    )
    await message.answer(
                'Отлично! Теперь опиши товар или услугу. Не более 800 символов.\n'
                # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                , reply_markup = ReplyKeyboardRemove()
    )
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q5)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer5": answer}
    )
    await message.answer(
        'Супер! Назначай цену. Пиши одним числом и не забудь указать валюту. Можно и про торг тут указать.\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
    )
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q6)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer6": answer}
    )
    # Достаем переменные
    data = await state.get_data()
    adtype = data.get("answer1")
    city = data.get("answer2")
    forwarding = data.get("answer3")
    photo = data.get("answer4")
    bio = data.get("answer5")
    price = data.get("answer6")
    answer7 = data.get("answer7")
    #============================
    # Генерируем ссылку на автора
    # def createAuthorName(self, firstname='', lastname='', username='', userid=0):
        # AuthorName  = f'[{message.from_user.first_name}'
        # AuthorName += f' {message.from_user.last_name}' if message.from_user.last_name is not None else ''
        # AuthorName += f', @{message.from_user.username}' if message.from_user.username is not None else ''
        # AuthorName += f'](tg://user?id={message.from_user.id})'
        # return AuthorName
    authorname = message.from_user.get_mention()
    authorname += f', @{message.from_user.username}' if message.from_user.username is not None else ''
    #
    # def createADText(self, firstname='', lastname='', username='', userid=0):
    # userlink = createAuthorName(message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id)
    #
    forwarding = ', #пересыл' if forwarding == 'Да' else ''
    #
    #     # Убираем пробелы в хештегах и ограничиваем на длину 25 символов
    city = city.replace(" ", "")
    tcity = (city[:25]+'..') if len(city) > 25 else city
    tprice = (price[:25]+'..') if len(price) > 25 else price
    #
    #     # Ограничиваем длину сообщения в 800 символов
    tbio = (bio[:800]+'..') if len(bio) > 800 else bio
    # Экранируем подчерки и звездочки для формата строки Markdown
    tbio = tbio.replace('_','\\_')
    tbio = tbio.replace('*','\\*')

    adtext = (f'#{adtype.replace(" ", "")}, '
                  f'#{tcity}'
                  f'{forwarding}\n'
                  f'{tbio}\n'
                  f'Цена: {tprice}\n\n'
                  f'Автор: {authorname}'
                                )
    # ====================
    await state.update_data(
        {"adtext": adtext}
    )
    await message.answer('*Предварительный просмотр:*', parse_mode='Markdown')
    await message.answer(f"Тип: {adtype}\n"
                         f"Город: {city}\n"
                         f"Перессыл: {forwarding}\n"
                         f"Фото: {photo}\n"
                         f"Текст объявления: {bio}\n"
                         f"Цена: {price}\n"
                         f"Автор: {authorname}")
    await message.answer(adtext)
    await message.answer('*Публикуем?*', parse_mode='Markdown'
                         , reply_markup=yesno_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q7)
async def answer_q7(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer7": answer}
    )
    # Достаем переменные
    data = await state.get_data()
    adtext = data.get("adtext")
    #
    await message.answer('*Ок!*', parse_mode='Markdown'
                , reply_markup = ReplyKeyboardRemove())
    await message.answer(adtext)
    await message.answer(f'Объявление опубликовано (нет) в группе {str(channel_name)}.' 
                              f'\nХорошего дня!'
                              f'\n/start чтобы начать с начала',
                           reply_markup=choice)
    # Вариант завершения1
    # await state.finish()

#     Вариант завершения 2
#     await state.reset_state()

#     Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
