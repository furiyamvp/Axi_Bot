from aiogram import types
from loader import dp
from utils.db_commands.film import get_film_code, get_film_link_instagram, get_film_link_you_tube, update_view_quantity
import re

from utils.db_commands.users import get_user, add_user
from utils.function.film import film_type_hashtag, film_view_quantity


@dp.message_handler(regexp=re.compile("^\\d{3}$"), chat_type=types.ChatType.PRIVATE)
async def user_search_film_handler(message: types.Message):
    film = await get_film_code(int(message.text))
    if await get_user(int(message.chat.id)):
        if film:
            view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
            if view_quantity:
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)

            else:
                await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)

        else:
            text = "Bunday kodli li kino yoq ❗️"
            await message.answer(text=text)
    else:
        if await add_user(message):
            if film:
                view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
                if view_quantity:
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)

                else:
                    await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)

            else:
                text = "Bunday kodli li kino yoq ❗️"
                await message.answer(text=text)


@dp.message_handler(regexp=r"^https:\/\/(www\.)?instagram\.com\/.*$", chat_type=types.ChatType.PRIVATE)
async def user_search_film_code_handler(message: types.Message):
    instagram_link = str(message.text.split("=")[0])
    film = await get_film_link_instagram(instagram_link)

    if await get_user(int(message.chat.id)):
        if film:
            view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
            if view_quantity:
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)

            else:
                await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)
        else:
            text = "Bunday link li kino yoq ❗️"
            await message.answer(text=text)
    else:
        if await add_user(message):
            if film:
                view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
                if view_quantity:
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)

                else:
                    await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)
                await message.answer_video(video=film["film"], caption=caption)
            else:
                text = "Bunday link li kino yoq ❗️"
                await message.answer(text=text)


@dp.message_handler(
    regexp=r"(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:watch\?v=|embed\/|shorts\/)|youtu\.be\/)([a-zA-Z0-9_-]{11})")
    , chat_type=types.ChatType.PRIVATE
async def user_search_film_code_handler(message: types.Message):
    you_tube_link = str(message.text.split("=")[0])
    film = await get_film_link_you_tube(you_tube_link)
    if await get_user(int(message.chat.id)):
        if film:
            view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
            if view_quantity:
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)

            else:
                await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                film_type = await film_type_hashtag(film["type"])

                caption = (
                    f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                    f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                    f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                await message.answer_video(video=film["film"], caption=caption)
            await message.answer_video(video=film["film"], caption=caption)
        else:
            text = "Bunday link li kino yoq ❗️"
            await message.answer(text=text)
    else:
        if await add_user(message):
            if film:
                view_quantity = await film_view_quantity(view_quantity=film["view_quantity"], chat_id=message.chat.id)
                if view_quantity:
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)

                else:
                    await update_view_quantity(film_id=film["id"], chat_id=message.chat.id)
                    film_type = await film_type_hashtag(film["type"])

                    caption = (
                        f"🆔Kino kodi: {film['code']}\n🎬Nomi: {film['name']}\n➖➖➖➖➖➖➖➖➖➖\n📀Sifati: {film['quality']}\n🌍Davlati: {film['state']}\n"
                        f"📅Sanasi: {film['date']}-yil\n🎞️Turi: {film_type}\n💜Instagram: {film['instagram']}\n"
                        f"❤️You Tube: {film['you_tube']}\n🧩Bizning kanalimiz: @Zangoriekrankanali")
                    await message.answer_video(video=film["film"], caption=caption)
                await message.answer_video(video=film["film"], caption=caption)
            else:
                text = "Bunday link li kino yoq ❗️"
                await message.answer(text=text)
