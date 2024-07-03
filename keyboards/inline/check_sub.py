from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


subs_check = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="Check", callback_data="check_subs")
    ]]
)
