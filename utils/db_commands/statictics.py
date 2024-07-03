from sqlalchemy import select, func

from main.database import database
from main.models import films


async def quantity_films():
    try:
        query = select(func.count(films.c.id))
        row = await database.fetch_one(query=query)
        return dict(row) if row else False
    except Exception as e:
        error_text = f"Error in quantity_film: {e}"
        print(error_text)
