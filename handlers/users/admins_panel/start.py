from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.admin import admin_main_menu_def
from loader import dp
from main.config import ADMINS


@dp.message_handler(CommandStart(), chat_id=ADMINS, state="*")
async def admin_start_handler(message: types.Message):
    text = "Hello Admin🫡"
    await message.answer(text=text, reply_markup=await admin_main_menu_def())
