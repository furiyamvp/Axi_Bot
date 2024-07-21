from typing import Union, Any
import random

from sqlalchemy import select
from sqlalchemy.sql import func

from main.database import database
from main.models import films


async def get_film_code(film_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.code == film_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_id}: {e}"
        print(error_text)


async def get_film_link_instagram(film_link: str) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.instagram == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


async def get_film_film(film_id: int) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.film == film_id)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_id}: {e}"
        print(error_text)


async def get_film_link_tiktok(film_link: str) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.tiktok == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


async def get_film_link_you_tube(film_link: str) -> Union[dict[Any, Any], bool]:
    try:
        query = select(films).where(films.c.you_tube == film_link)
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error retrieving user with ID {film_link}: {e}"
        print(error_text)


async def generate_unique_code():
    while True:
        code = random.randint(100, 999)
        query = select(films.c.code).where(films.c.code == code)
        existing_code = await database.fetch_one(query)
        if not existing_code:
            return code


async def add_film(data: dict):
    try:
        unique_code = await generate_unique_code()
        query = films.insert().values(
            film=data.get('film'),
            name=data.get('name'),
            language=None,
            quality=int(data.get('quality')),
            state=data.get('state'),
            date=int(data.get('date')),
            type=data.get('type'),
            instagram=data.get('instagram'),
            you_tube=data.get('you_tube'),
            status=data.get('status'),
            code=unique_code,
            created_at=data.get('created_at')
        ).returning(films.c.id)
        return await database.execute(query)

    except Exception as e:
        error_text = f"Error adding film: {e}"
        print(error_text)
        return None
