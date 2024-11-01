from aiogram import types
from keyboards.default.user import user_main_menu_def
from loader import dp


@dp.message_handler(text="Call-markaz 📞", state="*", chat_type=types.ChatType.PRIVATE)
async def call_center_handler(message: types.Message):
    text = """
1) @Misteraxi
2) @Zangori_Ekran_Admin
"""
    await message.answer(text=text, reply_markup=await user_main_menu_def())
