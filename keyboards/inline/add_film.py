from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


add_film_status = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Tekin 🆓", callback_data="Free"),
            InlineKeyboardButton(text="Premium 💎", callback_data="Premium"),
        ]
    ]
)


add_film_confirmation: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="Add"),
            InlineKeyboardButton(text="❌", callback_data="Not_add"),
        ]
    ]
)

