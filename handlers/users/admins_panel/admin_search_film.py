from aiogram import types

from keyboards.inline.change_film import admin_film_change_def
from loader import dp
from main.config import ADMINS
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_tiktok, get_film_link_you_tube
import re

from utils.function.film_type import film_type_hashtag


@dp.message_handler(regexp=re.compile("^\\d{3}$"), chat_id=ADMINS)
async def user_search_film_code(message: types.Message):
    film = await get_film_code(int(message.text))
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"🖤Tiktok: {film['tiktok']}\n❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = "Bunday kodli kino yo'q❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$", chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_link_instagram(message.text)
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = "Bunday link li kino yo'q ❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(vt\.)?tiktok\.com\/.*$", chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    instagram_link = str(message.text.split("=")[0])
    film = await get_film_link_tiktok(instagram_link)
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = "Bunday link li kino yo'q ❗️"
        await message.answer(text=text)


@dp.message_handler(
    regexp=r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})",
    chat_id=ADMINS)
async def user_search_film_code_handler(message: types.Message):
    you_tube_link = str(message.text.split("=")[0])
    film = await get_film_link_you_tube(you_tube_link)
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption,
                                   reply_markup=await admin_film_change_def(film['id']))
    else:
        text = "Bunday link li kino yo'q ❗️"
        await message.answer(text=text)
