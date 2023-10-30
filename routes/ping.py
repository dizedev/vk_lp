from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot
import time


async def get_ping(message: Message, answer: str) -> str:
    delta = round(time.time() - message.date, 2)

    if delta < 0:
        delta = "666"

    return f"{answer} Модуль Impulse LP\n" \
           f"Ответ через {delta} с"


@bl.message(Permission(), text=[prefix_bot + " пинг"])
async def ping_(message: Message):
    await edit_message(
        message,
        await get_ping(message, "ПОНГ")
    )
