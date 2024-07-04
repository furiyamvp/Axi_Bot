from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.user import user_main_menu_def
from loader import dp


@dp.message_handler(CommandStart(), state="*")
async def admin_start_handler(message: types.Message):
    text = "Botizmiga xush kelibsiz 🫡"
    await message.answer(text=text, reply_markup=await user_main_menu_def())
