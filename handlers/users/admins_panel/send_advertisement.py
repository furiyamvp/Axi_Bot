from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from main.config import ADMINS
from states.SendAdvertisement import SendAdvert
from utils.db_commands.users import get_all_users_chat_ids


@dp.message_handler(text="Reklama yuborish 🪧", chat_id=ADMINS, state="*")
async def stickers_menu(message: types.Message):
    text = "Iltimos ,reklamani video yokida rasmini yuboring."
    await message.answer(text=text)
    await SendAdvert.file.set()


@dp.message_handler(state=SendAdvert.file, chat_id=ADMINS, content_types=types.ContentType.VIDEO)
async def add_advertisement_file_handler(message: types.Message, state: FSMContext):
    await state.update_data(file=message.video.file_id, file_type="video")
    text = "Iltimos, reklamani tavsifini kiriting."
    await message.answer(text=text)
    await SendAdvert.description.set()


@dp.message_handler(state=SendAdvert.file, chat_id=ADMINS, content_types = types.ContentType.PHOTO)
async def add_advertisement_file_handler(message: types.Message, state: FSMContext):
    await state.update_data(file=message.photo[0].file_id, file_type="photo")
    text = "Iltimos, reklamani tavsifini kiriting."
    await message.answer(text=text)
    await SendAdvert.description.set()


@dp.message_handler(state=SendAdvert.description, chat_id=ADMINS)
async def add_advertisement_desc_send_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    users_id = await get_all_users_chat_ids()

    if data["file_type"] == "video":
        for user_id in users_id:
            await dp.bot.send_video(chat_id=user_id, video=data["file"], caption=message.text)
    elif data["file_type"] == "photo":
        for user_id in users_id:
            await dp.bot.send_photo(chat_id=user_id, photo=data["file"], caption=message.text)
    else:
        await message.answer(text="Xatolik yuzberdi")

    await state.finish()


