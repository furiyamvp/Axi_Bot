from aiogram import types
from loader import dp


@dp.message_handler()
async def error_message(message: types.Message):
    if message.text.isdigit():
        text = "Kino kodi 3 xonli son bo'ladi"
        await message.answer(text=text)
    else:
        text = (
            "Iltimos botga har qanday sozlarni yozib tashlamang, Bot orqali siz bizni kinolarimni korishingiz mumkin "
            "kino topish uchun bizni instagram kanalimizdagi yokida tiktokdagi kanalimizdagi kinoni videoni linkini "
            "olib botga tashlasangiz kino chiqib keladi, kinoni kodi bilan ham topsangiz boladi, kino kodi har "
            "qachon 3 xonali boladi"
        )
        await message.answer(text=text)
