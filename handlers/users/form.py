from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp
from states.test import AdvertQA


# Сделаем фильтр на комманду /test, где не будет указано никакого состояния
@dp.message_handler(Command("form"), state=None)
async def enter_test(message: types.Message):
    await message.answer("Введите свое имя")
    # Вариант 1 - с помощью функции сет
    await AdvertQA.Q1.set()
    # Вариант 2 - с помощью first
    # await AdvertQA.first() или ранее Test.first()


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
    await message.answer("Введите свой email")
    await AdvertQA.next()
    # await Test.Q2.set()


@dp.message_handler(state=AdvertQA.Q2)
async def answer_q1(message: types.Message, state: FSMContext):
    answer = message.text
    await state.update_data(
        {"answer2": answer}
    )

    await message.answer("Введите свой телефон")
    await AdvertQA.next()


@dp.message_handler(state=AdvertQA.Q3)
async def answer_q2(message: types.Message, state: FSMContext):
    # Достаем переменные
    data = await state.get_data()
    answer1 = data.get("answer1")
    answer2 = data.get("answer2")
    answer3 = message.text
    #
    await message.answer("Привет! Ты ввел следующие данные:\n"
                         f"Имя - \"{answer1}\"\n"
                         f"Email - \"{answer2}\"\n"
                         f"Телефон - \"{answer3}\"")

    # Вариант завершения1
    # await state.finish()

#     Вариант завершения 2
#     await state.reset_state()

#     Вариант завершения 3 - без стирания данных в data
    await state.reset_state(with_data=False)
