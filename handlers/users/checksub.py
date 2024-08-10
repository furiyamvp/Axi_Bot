from aiogram import types

from keyboards.inline.check_sub import subs_check
from loader import dp
from main.config import CHANNELS
from utils.misc import subscription
from keyboards.default.user import user_main_menu_def


@dp.callback_query_handler(text="check_subs", state="*")
async def check_subs_handler(call: types.CallbackQuery):
    result = "Botdan foydalanish uchun quyidagi kanalga obuna bo'ling:\n"
    final_status = True
    for channel in CHANNELS:
        status = await subscription.check(user_id=call.message.chat.id, channel=channel[1])
        if not status:
            final_status = False
            result += f"👉 <a href='{channel[0]}'>{channel[-1]}</a>\n"
    if not final_status:
        await call.message.answer(result, disable_web_page_preview=True, reply_markup=subs_check)
    else:
        text = "😊 Assalomu alaykum"
        await call.message.answer(text=text, reply_markup=await user_main_menu_def())