from aiogram import types
from loader import dp

@dp.message_handler()
async def error_message_text_handler(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        if message.text.isdigit():
            text = "Kino kodi 3 xonli son bo'ladi"
            await message.answer(text=text)
        else:
            text = (
                "Iltimos botga har qanday sozlarni yozib tashlamang, Bot orqali siz bizni kinolarimni korishingiz mumkin. "
                "Kino topish uchun bizni Instagram kanalimizdagi yoki TikTokdagi kanalimizdagi kinoni videoni linkini "
                "olib botga tashlasangiz kino chiqib keladi, kinoni kodi bilan ham topsangiz boladi, kino kodi har "
                "qachon 3 xonali bo'ladi."
            )
            await message.answer(text=text)

@dp.message_handler(content_types=types.ContentType.ANY)
async def error_message_all_handler(message: types.Message):
    if message.chat.type == types.ChatType.PRIVATE:
        text = (
            "Iltimos botga har qanday narsalar tashlamang, Bot orqali siz bizni kinolarimni korishingiz mumkin. "
            "Kino topish uchun bizni Instagram kanalimizdagi yoki TikTokdagi kanalimizdagi kinoni videoni linkini "
            "olib botga tashlasangiz kino chiqib keladi, kinoni kodi bilan ham topsangiz boladi, kino kodi har "
            "qachon 3 xonali bo'ladi."
        )
        await message.answer(text=text)
