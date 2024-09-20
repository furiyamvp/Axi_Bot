from typing import Optional


async def film_type_hashtag(film_type: str):
    type_strip = film_type.strip()
    type_template_fist_latter = type_strip[0]
    type = type_strip.replace(" ", " #").replace(f"{type_template_fist_latter}",
                                                 f"#{type_template_fist_latter}")
    return type


async def film_view_quantity(view_quantity: Optional[str], chat_id: int):
    if not view_quantity:
        return False
    view_quantity = view_quantity.strip().split(" ")

    for user_chat_id in view_quantity:
        if user_chat_id == str(chat_id):
            return True
    return False
