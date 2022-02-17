from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp, bot
from aiogram.utils.markdown import hbold, hcode, hitalic, hunderline, hstrikethrough, hlink

html_text = "\n".join(
    [
        "Привет, " + hbold("Костя!"),
        "Как говорится:",
        hitalic("Бояться надо не смерти, а пустой жизни."),
        "",
        "Но мы сейчас не об этом. " + hstrikethrough("Что тебе нужно?"),
        "Этот текст с HTML форматированием. "
        "Почитать об этом можно " + hlink("тут",
                                          "https://core.telegram.org/bots/api#formatting-options"),
        hunderline("Внимательно прочти и используй с умом!"),
        "",
        hcode("Пример использования - ниже:"),
        "",
        ""]
)
html_text += hcode(html_text)


@dp.message_handler(Command("parse_mode_html"))
async def show_parse_mode(message: types.Message):
    await message.answer(html_text, parse_mode=types.ParseMode.HTML)
