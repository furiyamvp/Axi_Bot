from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def admin_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("Statistikalar 📊"),
            ],
            [
                KeyboardButton("Kino qo'shish ➕")
            ],
        ], resize_keyboard=True
    )
    return markup


async def statistics_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("Foydalanuvchilar soni 👥"),
                KeyboardButton("Filmlar soni 🎥")
            ],
            [
                KeyboardButton("Orqaga ⬅️")
            ],
        ], resize_keyboard=True
    )
    return markup
