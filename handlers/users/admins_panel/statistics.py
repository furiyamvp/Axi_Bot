from aiogram import types

from loader import dp
from main.config import ADMINS
from keyboards.default.admin import statistics_menu_def
from utils.db_commands.statictics import quantity_films


@dp.message_handler(text="Statistikalar 📊", chat_id=ADMINS, state="*")
async def statistics_menu_handler(message: types.Message):
    text = "Statistika sahifasiga xu"
    await message.answer(text=text, reply_markup=await statistics_menu_def())


@dp.message_handler(text="Filmlar soni 🎥", chat_id=ADMINS, state="*")
async def quantity_film_menu_handler(message: types.Message):
    quantity_film = await quantity_films()
    quantity_film_number = quantity_film["count_1"]
    text = f"Botda {quantity_film_number} ta film bor"
    await message.answer(text=text, reply_markup=await statistics_menu_def())
