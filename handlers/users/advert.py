import time

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove, InputFile, Update
from keyboards.default import startmenu, adtype_buttons, adtype2_buttons, country_buttons, city_buttons, yesno_buttons, photo_button, nextstep_button
from keyboards.inline.choice_buttons import choice, about, onwheel_keyboard, apples_keyboard
from data.config import channel_name, ADMINS, banned_users

from loader import dp, bot
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

user_id=ADMINS,


@dp.callback_query_handler(user_id=banned_users, text_contains="newad")
async def get_button(call: types.CallbackQuery):
    # call = message
    await call.message.edit_text(f'Вы находитесь в Блоклисте.\n'  # {call.message.from_user.first_name}, в - баг
                                      f'Вам недоступна эта функция.\n'
                                      f'Напишите модераторам',
        reply_markup=choice)


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
    await state.update_data(
        {"answer1": answer}
    )
    await message.answer('Какой подтип объявления?\n',
        reply_markup=adtype2_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer2": answer}
    )
    await message.answer('В какой стране ты находишься?\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                         , reply_markup=country_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q3)
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
        {"answer3": answer}
    )
#
#     # Вариант 3 - через state.proxy
#     async with state.proxy() as data:
#         data["answer1"] = answer
#         # Удобно, если нужно сделать data["some_digit"] += 1
#         # Или data["some_list"].append(1), т.к. не нужно сначала доставать из стейта, А потом задавать
#
    await message.answer(f'В каком городе ты находишься? Выбери или *напиши словом*\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                         , parse_mode='Markdown', reply_markup=city_buttons)
    await AdvertQA.next()
    # await Test.Q2.set()


@dp.message_handler(state=AdvertQA.Q4)
async def answer_q2(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer4": answer}
    )
    await message.answer('Отлично! Возможен ли пересыл почтой или ТК?\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                         , reply_markup=yesno_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q5)
async def answer_q3(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer5": answer}
    )
    await message.answer(
        'Не более 10 фото!!!\n'
        'Супер. Приложи фото. Пока не больше четырёх.\n'
        'Можешь в одном альбоме. Можешь по одной.\n'
        # 'Но десятое фото должно быть отдельно (Баг)\n'
        'Или /skip если фото не нужно.\n\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
        , reply_markup=photo_button)
    await AdvertQA.next()


# создается пустой элемент для персонификации для каждого объявления, иначе не персонифицируется
# ads = {0: Advert(['0'])}
ads = []


@dp.message_handler(state=AdvertQA.Q6)
async def answer_q4(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer6": answer}
    )
    await message.answer(
                'Отлично! Теперь опиши товар или услугу. Не более 800 символов.\n'
                # 'Пиши /cancel для остановки и сброса процесса.\n\n'
                , reply_markup = ReplyKeyboardRemove()
    )
    await AdvertQA.next()


@dp.message_handler(content_types=types.ContentType.PHOTO, state=AdvertQA.Q4)
async def get_file_id_p(message: types.Message, state: FSMContext):
    photo = message.photo[-1].file_id
    answer = message.photo[-1].file_id
    await state.update_data(
        {"answer7": answer}
    )
    # await message.answer(
    #             'Отлично! Теперь опиши товар или услугу. Не более 800 символов.\n'
    #             # 'Пиши /cancel для остановки и сброса процесса.\n\n'
    #             , reply_markup = ReplyKeyboardRemove()
    # )
    if len(ads) < 10:
        ads.append(photo)
        await message.answer(f'Загрузил... {len(ads)} фото \n{photo}', reply_markup = photo_button)
        if len(ads) >= 10:
            await message.answer('Отлично! Теперь опиши товар или услугу. Не более 800 символов.', reply_markup = ReplyKeyboardRemove())
            await AdvertQA.Q5.set()
            # ответ - мы прилетаем в AdvertQA.Q4 и снова идёт запрос описания товара или услуги.
        # else:
            # await AdvertQA.Q4()
    else:
        await message.answer(f'Загружено {len(ads)} фото ', reply_markup = ReplyKeyboardRemove())
        await message.answer('Ошибка! Больше 10 фото!\nОтлично! Теперь опиши товар или услугу. Не более 800 символов.\n',
                             reply_markup=ReplyKeyboardRemove())
        await AdvertQA.Q5.set()
    #
    # if len(ads[message.photo[-1].file_id]) <= 4:
    #     if photo.file_id not in ads[message.photo[-1].file_id]:
    #         ads[message.photo[-1].file_id.append(photo.file_id)
    #         # logger.info("Photo of %s: %s", user.first_name, photo.file_id)
    #         await message.answer(
    #             # Update.message.reply(#)
    #             # message.reply(message.photo[-1].file_id)
    #             # Update.message.reply(
    #             f'Загрузил... {photo}',
    #             reply_markup = photo_button,
    #         )
    #     if len(ads[message.photo[-1].file_id]) > 4:
    #         await Update.message.reply(
    #             'Отлично! Теперь опиши товар или услугу. Не более 800 символов.\n'
    #             # 'Пиши /cancel для остановки и сброса процесса.\n\n'
    #             , reply_markup = photo_button,
    #         )
    # await AdvertQA.Q4()


@dp.message_handler(state=AdvertQA.Q7)
async def answer_q5(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer7": answer}
    )
    await message.answer(
        'Супер! Назначай цену. Пиши одним числом и не забудь указать валюту. Можно и про торг тут указать.\n'
        # 'Пиши /cancel для остановки и сброса процесса.\n\n'
    )
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q8)
async def answer_q6(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer8": answer}
    )
    # Достаем переменные
    data = await state.get_data()
    adtype = data.get("answer1")
    adtype2 = data.get("answer2")
    Country = data.get("answer3")
    city = data.get("answer4")
    forwarding = data.get("answer5")
    photo = data.get("answer6")
    bio = data.get("answer7")
    price = data.get("answer8")
    answer9 = data.get("answer9")
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

    # формируем объявление:
    adtext = (f'#{adtype.replace(" ", "")}, #{adtype2.replace(" ", "")}, '
                  f'#{tcity}'
                  f'{forwarding}\n'
                  f'{tbio}\n'
                  f'Цена: {tprice}\n\n'
                  f'Автор: {authorname}'
                                )
    # ==================== сформированное объявление:
    await state.update_data(
        {"adtext": adtext}
    )
    await message.answer(f"Вводные данные (для отладки):\n"
                         f"Тип: {adtype} {adtype2}\n"
                         f"Город: {city}\n"
                         f"Перессыл: {forwarding}\n"
                         f"Фото: {len(ads)}\n"
                         f"Текст объявления: {bio}\n"
                         f"Цена: {price}\n"
                         f"Автор: {authorname}")
    await message.answer('*Предварительный просмотр:*', parse_mode='Markdown')
    if len(ads) > 0:
        # Создаем альбом
        album = types.MediaGroup()
        album.attach_photo(photo=ads[0], caption=adtext)
        for a in ads[1:]:
            album.attach_photo(photo=a)  # , caption=adtext)
        await message.answer_media_group(media=album)
    else:
        await message.answer(adtext)
    await message.answer('*Публикуем?*', parse_mode='Markdown'
                         , reply_markup=yesno_buttons)
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q9)
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
    if answer == "Да":
        if len(ads) > 0:
            # Создаем альбом, опять...
            album = types.MediaGroup()
            album.attach_photo(photo=ads[0], caption=adtext)
            for a in ads[1:]:
                album.attach_photo(photo=a)  # , caption=adtext)
            await message.answer_media_group(media=album)
            await bot.send_media_group(chat_id=channel_name, media=album)
        else:
            await message.answer(adtext)
            await bot.send_message(chat_id=channel_name, text=adtext)
        await message.answer(f'Объявление опубликовано в группе {str(channel_name)}.' 
                              f'\nХорошего дня!'
                              f'\n/start чтобы начать с начала',
                           reply_markup=choice)
        ads.clear()
    else:
        await message.answer(f'Объявление *не* опубликовано', parse_mode='Markdown', reply_markup=choice)
        ads.clear()
    # Вариант завершения1
    # await state.finish()

#     Вариант завершения 2
#     await state.reset_state()

#     Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
