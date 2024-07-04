from aiogram import types
from loader import dp
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_you_tube
import re

from utils.function.film_type import film_type_hashtag


@dp.message_handler(regexp=re.compile("^\\d{3}$"))
async def user_search_film_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption)

    else:
        text = "Bunday kodli li kino yoq ❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$")
async def user_search_film_code_handler(message: types.Message):
    instagram_link = str(message.text.split("=")[0])
    film = await get_film_link_instagram(instagram_link)
    print(film)
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption)
    else:
        text = "Bunday link li kino yoq ❗️"
        await message.answer(text=text)


@dp.message_handler(
    regexp=r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})")
async def user_search_film_code_handler(message: types.Message):
    you_tube_link = str(message.text.split("=")[0])
    print(you_tube_link)
    film = await get_film_link_you_tube(you_tube_link)
    if film:
        film_type = await film_type_hashtag(film["type"])

        caption = (
            f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
            f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
            f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekran_kanali")
        await message.answer_video(video=film["film"], caption=caption)
    else:
        text = "Bunday link li kino yoq ❗️"
        await message.answer(text=text)
