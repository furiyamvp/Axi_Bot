from aiogram.dispatcher.filters.state import StatesGroup, State


class SendAdvert(StatesGroup):
    file = State()
    file_type = State()
    description = State()

