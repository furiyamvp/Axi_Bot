from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.default.admin import admin_main_menu_def
from keyboards.inline.add_film import add_film_status, add_film_confirmation
from main.config import ADMINS

from loader import dp
from states.AddFilmState import AddFilm
from keyboards.default.back import main_menu_back
from utils.checker.checker_link import check_link_instagram, check_link_you_tube
from utils.db_commands.film import add_film
from utils.function.film_type import film_type_hashtag


@dp.message_handler(text="Kino qo'shish ➕", state="*", chat_id=ADMINS)
async def add_product_handler(message: types.Message):
    text = "Iltimos filmni kiriting"
    await message.answer(text=text, reply_markup=await main_menu_back())
    await AddFilm.film.set()


@dp.message_handler(state=AddFilm.film, chat_id=ADMINS, content_types=types.ContentType.VIDEO)
async def add_product_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(film=message.video.file_id)
    await state.update_data(quality=message.video.height)
    text = ("Iltimos kinoni nomini kiriting.\n"
            "Masalan: Harry Potter")
    await message.answer(text=text)
    await AddFilm.name.set()


@dp.message_handler(state=AddFilm.film)
async def error_photo_handler(message: types.Message):
    text = "Siz faqat kino tashlay olasiz so'z kirita olmaysiz"
    await message.answer(text=text)
    await AddFilm.film.set()


@dp.message_handler(state=AddFilm.name, chat_id=ADMINS)
async def add_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    text = ("Iltimos kino qaysi davlatni kinosiligini kitiying\n"
            "Masalan: USA")
    await message.answer(text=text)
    await AddFilm.state.set()


@dp.message_handler(state=AddFilm.state, chat_id=ADMINS)
async def add_state_handler(message: types.Message, state: FSMContext):
    await state.update_data(state=message.text)
    text = ("Iltimos kino chiqarilgan yilini kiriting\n"
            "Masalan: 2024")
    await message.answer(text=text)
    await AddFilm.date.set()


@dp.message_handler(state=AddFilm.date, chat_id=ADMINS)
async def add_date_handler(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    text = ("Iltimos Kino turini kiritin bir neshta kiritsangiz ham boladi\n"
            "Masalan: Jangar Fantastika Horor, vergul va boshqa narsalardan foydalanmang")
    await message.answer(text=text)
    await AddFilm.type.set()


@dp.message_handler(state=AddFilm.type, chat_id=ADMINS)
async def add_type_handler(message: types.Message, state: FSMContext):
    await state.update_data(type=message.text)
    text = ("Iltimos Kinoni instagramdagi qisqa videosini link ni kiriting \n"
            "Masalan: https://www.instagram.com/******")
    await message.answer(text=text)
    await AddFilm.instagram.set()


@dp.message_handler(state=AddFilm.instagram, chat_id=ADMINS)
async def add_instagram_link_handler(message: types.Message, state: FSMContext):
    if await check_link_instagram(message.text):
        instagram_link = message.text.split("=")[0]
        await state.update_data(instagram=instagram_link)
        text = ("Iltimos Kinoni tiktokdagi qisqa videosini link ni kiriting\n"
                "Masalan: https://www.youtube.com/******")
        await message.answer(text=text)
        await AddFilm.you_tube.set()
    else:
        text = "Faqat instagramni linkini kirita olasiz"
        await message.answer(text=text)
        await AddFilm.instagram.set()


@dp.message_handler(state=AddFilm.you_tube, chat_id=ADMINS)
async def add_you_tube_link_handler(message: types.Message, state: FSMContext):
    if await check_link_you_tube(message.text):
        you_tube_link = message.text.split("=")[0]
        await state.update_data(you_tube=you_tube_link)
        text = ("Kinoni statusi qanday bolsin ?\n"
                "Example: Free or Premium")
        await message.answer(text=text, reply_markup=add_film_status)
        await AddFilm.status.set()
    else:
        text = "you can only enter an tiktok link"
        await message.answer(text=text)
        await AddFilm.you_tube.set()


@dp.callback_query_handler(state=AddFilm.status, text="Premium", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "Film Qo'shilsinmi ? ➕"
    await state.update_data(status="Premium")
    await call.message.answer(text=text, reply_markup=add_film_confirmation)
    await AddFilm.confirmation.set()


@dp.callback_query_handler(state=AddFilm.status, text="Free", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "Film Qo'shilsinmi ? ➕"
    await state.update_data(status="Free")
    await call.message.answer(text=text, reply_markup=add_film_confirmation)
    await AddFilm.confirmation.set()


@dp.callback_query_handler(state=AddFilm.confirmation, text="Add", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    date = await state.get_data()
    if await add_film(date):
        film_type = await film_type_hashtag(date["type"])
        text = "Movie added. ✅"

        caption = (f"\n🎬Nomi: {date['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {date['quality']}\n🌍state: {date['state']}\n"
                   f"📅Date: {date['date']}-year\n🎞️type: {film_type}\n💜Instagram: {date['instagram']}\n"
                   f"❤️You Tube: {date['you_tube']}")
        await call.message.answer_video(video=date["film"], caption=caption)
        await call.message.answer(text=text)
        await state.finish()
    else:
        text = "Kino qoshish joyida xatolik chiqdi ❌"
        await call.message.answer(text=text, reply_markup=await admin_main_menu_def())


@dp.callback_query_handler(state=AddFilm.confirmation, text="Not_add", chat_id=ADMINS)
async def add_status_handler(call: CallbackQuery, state: FSMContext):
    text = "Kino qoshish toxtatildi 🛑"
    await call.message.answer(text=text, reply_markup=await admin_main_menu_def())
    await state.finish()
