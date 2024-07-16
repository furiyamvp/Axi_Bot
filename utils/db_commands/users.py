from typing import Any, Union

from main.database import database
from main.models import *


async def get_user(chat_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = users.select().where(users.c.chat_id == chat_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error get user with ID {chat_id}: {e}"
        print(error_text)


async def add_user(message):
    try:
        query = users.insert().values(
            chat_id=message.chat.id,
            created_at=message.date
        )
        await database.execute(query)
        return True
    except Exception as e:
        error_text = f"Error adding user: {e}"
        print(error_text)
