from aiogram import types
from keyboards.default.back import main_menu_back
from loader import dp


@dp.message_handler(text="Call-markaz 📞", state="*")
async def call_center_handler(message: types.Message):
    text = """
1) @Misteraxi
2) @furiya_yunus
"""
    await message.answer(text=text, reply_markup=await main_menu_back())
