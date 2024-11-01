from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils.exceptions import BotBlocked

from loader import dp
from main.config import ADMINS
from states.SendAdvertisement import SendAdvert
from utils.db_commands.users import get_all_users_chat_ids


@dp.message_handler(text="Reklama yuborish 🪧", chat_id=ADMINS, state="*")
async def stickers_menu(message: types.Message):
    text = "Iltimos, reklamani video yoki rasmlarini yuboring. Yuborishni tugatish uchun /stop buyrug'ini kiriting."
    await message.answer(text=text)
    await SendAdvert.file.set()


@dp.message_handler(state=SendAdvert.file, chat_id=ADMINS, content_types=types.ContentType.PHOTO)
async def add_advertisement_file_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])
    photos.append(message.photo[-1].file_id)
    await state.update_data(photos=photos)

    await message.answer("Rasm qo'shildi. Yana rasm yuboring yoki /stop buyrug'ini kiriting.")


@dp.message_handler(state=SendAdvert.file, chat_id=ADMINS, content_types=types.ContentType.VIDEO)
async def add_advertisement_video_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    videos = data.get('videos', [])
    videos.append(message.video.file_id)
    await state.update_data(videos=videos)

    await message.answer("Video qo'shildi. Yana video yoki rasm yuboring yoki /stop buyrug'ini kiriting.")


@dp.message_handler(commands="stop", state=SendAdvert.file, chat_id=ADMINS)
async def stop_adding_files(message: types.Message, state: FSMContext):
    await message.answer("Iltimos, reklamani tavsifini kiriting.")
    await SendAdvert.description.set()


import re


def escape_markdown(text: str) -> str:
    # Escape MarkdownV2 special characters
    return re.sub(r'([_`*!~[\](){}<>#+\-.|])', r'\\\1', text)


def format_message(description: str) -> str:
    # Example of formatting with bold, italics, and blockquotes
    # You can customize this function to match your specific formatting needs
    formatted_description = description
    formatted_description = formatted_description.replace('**', '*')  # Adjusting to MarkdownV2
    formatted_description = formatted_description.replace('*', '*')  # Bold
    formatted_description = formatted_description.replace('_', '*')  # Italics
    formatted_description = formatted_description.replace('`', '```')  # Code

    # Adding blockquote formatting (if you want to treat any line as a blockquote)
    lines = formatted_description.split('\n')
    formatted_description = '\n'.join(f'> {line}' for line in lines if line.strip())

    return formatted_description


@dp.message_handler(state=SendAdvert.description, chat_id=ADMINS)
async def add_advertisement_desc_send_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    photos = data.get('photos', [])
    videos = data.get('videos', [])
    users_id = await get_all_users_chat_ids()
    description = message.text

    for user_id in users_id:
        if user_id in ADMINS:
            continue

        try:
            if photos:
                media_group = types.MediaGroup()
                for photo in photos:
                    media_group.attach_photo(photo)

                await dp.bot.send_media_group(chat_id=user_id, media=media_group)
                await dp.bot.send_message(chat_id=user_id, text=description)

            elif videos:  # Check if there are videos
                for video in videos:
                    await dp.bot.send_video(chat_id=user_id, video=video, caption=description)

            else:  # No photos or videos, send text message
                # Format the description for MarkdownV2
                formatted_description = format_message(description)
                escaped_description = escape_markdown(formatted_description)

                # Send the escaped and formatted message with MarkdownV2 parsing
                await dp.bot.send_message(chat_id=user_id, text=escaped_description, parse_mode='MarkdownV2')

        except BotBlocked:
            pass
        except Exception as e:
            print(f"Xato: {e}")

    await message.answer("Reklama muvaffaqiyatli jo'natildi!")
    await state.finish()
