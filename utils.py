import time

from vkbottle.user import Message

rewards = {
    "discoverer": "Первооткрыватель",
    "creator": "Создатель",
    "admin": "Администратор",
    "moderator": "Moderator",
    "researcher": "Исследователь",
    "sponsor": "Спонсор"
}

next_line_symbol = "\n"


async def ping(message: Message, answer: str) -> str:
    delta = round(time.time() - message.date, 2)

    if delta < 0:
        delta = "666"

    return f"{answer} Модуль Impulse LP\n" \
           f"Ответ через {delta} с"
