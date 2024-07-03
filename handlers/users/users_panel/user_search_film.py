from aiogram import types
from loader import dp
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_tiktok, get_film_link_you_tube
from utils.db_commands.users import get_user_status
from keyboards.default.user import user_main_menu_def
import re

from utils.function.film_type import film_type_hashtag


@dp.message_handler(regexp=re.compile("^\\d{3}$"))
async def user_search_film_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    film_status = dict(film)["status"]
    user_status = await get_user_status(int(message.chat.id))
    if film:
        if film_status == "Premium" and user_status == "Free":
            text = (
                "Bu kinoni ko'rishingiz uchun premium imizni sotib olgan bo'lishingiz kerak premium narxi 10.000 so'm\n"
                "👤Admin @Misteraxi")
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            film_type = await film_type_hashtag(film["type"])

            caption = (f"🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍state: {film['state']}\n"
                       f"📅Date: {film['date']}-year\n🎞️type: {film_type}\n💜Instagram: {film['instagram']}\n"
                       f"🖤Tiktok: {film['tiktok']}\n❤️You Tube: {film['you_tube']}\n🧩Our Chanel: @Zangoriekran_kanali")
            await message.answer_video(video=film["film"], caption=caption)

    else:
        text = "Bunday kodli li kino yoq ❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$")
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    film_status = dict(film)["status"]
    user_status = await get_user_status(int(message.chat.id))
    if film:
        if film_status == "Premium" and user_status == "Free":
            text = (
                "Bu kinoni ko'rishingiz uchun premium imizni sotib olgan bo'lishingiz kerak premium narxi 10.000 so'm\n"
                "👤Admin @Misteraxi")
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            film_type = await film_type_hashtag(film["type"])

            caption = (f"🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍state: {film['state']}\n"
                       f"📅Date: {film['date']}-year\n🎞️type: {film_type}\n💜Instagram: {film['instagram']}\n"
                       f"🖤Tiktok: {film['tiktok']}\n❤️You Tube: {film['you_tube']}\n🧩Our Chanel: @Zangoriekran_kanali")
            await message.answer_video(video=film["film"], caption=caption)

    else:
        text = "Bunday link li kino yoq ❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(vt\.)?tiktok\.com\/.*$")
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    film_status = dict(film)["status"]
    user_status = await get_user_status(int(message.chat.id))
    if film:
        if film_status == "Premium" and user_status == "Free":
            text = (
                "Bu kinoni ko'rishingiz uchun premium imizni sotib olgan bo'lishingiz kerak premium narxi 10.000 so'm\n"
                "👤Admin @Misteraxi")
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            film_type = await film_type_hashtag(film["type"])

            caption = (f"🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍state: {film['state']}\n"
                       f"📅Date: {film['date']}-year\n🎞️type: {film_type}\n💜Instagram: {film['instagram']}\n"
                       f"🖤Tiktok: {film['tiktok']}\n❤️You Tube: {film['you_tube']}\n🧩Our Chanel: @Zangoriekran_kanali")
            await message.answer_video(video=film["film"], caption=caption)

    else:
        text = "Bunday link li kino yoq ❗️"
        await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?(youtube\.com\/|youtu\.be\/).*")
async def user_search_film_code_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    film_status = dict(film)["status"]
    user_status = await get_user_status(int(message.chat.id))
    if film:
        if film_status == "Premium" and user_status == "Free":
            text = (
                "Bu kinoni ko'rishingiz uchun premium imizni sotib olgan bo'lishingiz kerak premium narxi 10.000 so'm\n"
                "👤Admin @Misteraxi")
            await message.answer(text=text, reply_markup=await user_main_menu_def())
        else:
            film_type = await film_type_hashtag(film["type"])

            caption = (f"🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍state: {film['state']}\n"
                       f"📅Date: {film['date']}-year\n🎞️type: {film_type}\n💜Instagram: {film['instagram']}\n"
                       f"🖤Tiktok: {film['tiktok']}\n❤️You Tube: {film['you_tube']}\n🧩Our Chanel: @Zangoriekran_kanali")
            await message.answer_video(video=film["film"], caption=caption)

    else:
        text = "Bunday link li kino yoq ❗️"
        await message.answer(text=text)