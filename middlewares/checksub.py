from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from main.config import CHANNELS, ADMINS
from utils.misc.subscription import check
from keyboards.inline.check_sub import subs_check
from loader import dp


class BigBrother(BaseMiddleware):
    async def on_pre_process_update(self, update: types.Update, data: dict):
        if update.message:
            user = update.message.from_user.id
        elif update.callback_query:
            user = update.callback_query.from_user.id
            if update.callback_query.data == "check_subs" or str(user) in ADMINS:
                return
        else:
            return

        result = "Botdan foydalanish uchun kanalga obuna bo'ling:\n"
        final_status = True
        for channel in CHANNELS:
            status = await check(user_id=user, channel=channel[1])
            if not status:
                final_status = False
                result += f"👉 <a href='{channel[0]}'>{channel[-1]}</a>\n"
        if not final_status:
            await update.message.answer(result, disable_web_page_preview=True, reply_markup=subs_check)
            raise CancelHandler()