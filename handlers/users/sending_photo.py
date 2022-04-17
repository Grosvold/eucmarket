from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(content_types=types.ContentType.PHOTO)
async def get_file_id_p(message: types.Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=types.ContentType.VIDEO)
async def get_file_id_v(message: types.Message):
    await message.reply(message.video.file_id)


@dp.message_handler(Command("get_photo"))
async def send_cat(message: types.Message):
    photo = "AgACAgIAAxkBAAIKlWJbovMm5Z8RbeBHcTPgRKDb3M3IAALOuTEbvjbgSlW6efLz6FrqAQADAgADeQADJAQ"  # File id
    # photo = "https://www.meme-arsenal.com/memes/3f5777727d3f6e263b4edbee5bd15a1b.jpg" # URL
    # photo = InputFile(path_or_bytesio="photos/cat.jpg")  # Local file
    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption="Вот тебе фото кота /more_photos")


@dp.message_handler(Command("more_photos"))
async def more_cats(message: types.Message):
    # Создаем альбом
    album = types.MediaGroup()

    # Прикрепляем фото и видео
    # Максимум в альбоме 10 медиа. Максим 1 видео в аольбоме. Видео можно воткнуть в любое место.
    photo_file_id = "AgACAgIAAxkBAAIKkWJbop37y9ie2MY0EH0mPy8kixnGAALLuTEbvjbgSlGk9PQgX5UIAQADAgADeQADJAQ"
    photo_url = "https://i.pinimg.com/originals/13/25/68/132568dbe8f3316aa56551dba527e7f7.jpg"
    # photo_bytes = InputFile("photos/cat.jpg")
    video_file_id = "BAACAgIAAxkBAAIKM2JbnZZzuimxMHoDAhBPuJ4crHHaAAJREgAC8cmQSfYSjtAQ7VWSJAQ"
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo_file_id)
    # album.attach_photo(photo=photo_file_id, caption="Прикольный котик")
    # album.attach_photo(photo=photo_url)
    # album.attach_photo(photo=photo_bytes)
    # album.attach_photo(video=video_file_id)
    album.attach_video(video=video_file_id,
                       caption="Видео где котик запрыгивает на кровать")
    album.attach_photo(photo=photo_file_id)
    album.attach_photo(photo=photo_file_id)

    # Отправляем
    # await bot.send_media_group(chat_id=message.from_user.id, media=album)
    await message.answer_media_group(media=album)