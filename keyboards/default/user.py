from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def user_main_menu_def():
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton("Call-markaz 📞"),
            ]
        ], resize_keyboard=True
    )
    return markup
