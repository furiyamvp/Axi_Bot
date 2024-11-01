from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.admin import admin_main_menu_def
from main.config import ADMINS
from loader import dp


@dp.message_handler(text="Orqaga ⬅️", user_id=ADMINS, state="*", chat_type=types.ChatType.PRIVATE)
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Bosh sahifaga xushkelib siz"
    await message.answer(text=text, reply_markup=await admin_main_menu_def())
    await state.finish()
