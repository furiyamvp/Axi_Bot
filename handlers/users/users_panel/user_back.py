from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.user import user_main_menu_def
from loader import dp


@dp.message_handler(text="Orqaga ⬅️", state="*")
async def stickers_menu(message: types.Message, state: FSMContext):
    text = "Bosh sahifaga xushkelib siz"
    await message.answer(text=text, reply_markup=await user_main_menu_def())
    await state.finish()
