import time

from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot, prefix_dd
from custom_rules.permission import Permission
from utils import rewards

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " профиль"])
async def get_profile_cmd(message: Message):
    delta = round(time.time() - message.date, 2)

    if delta < 0:
        delta = "666"

    await edit_message(message,
                       f"Твой профиль:\n\n Название бота: Impulse LP\n Твоя версия: None\n  Твои достижения:  {rewards[1]}️\n Твой префикс: {prefix_bot}\n Твой префикс дд: {prefix_dd}\n Твой пинг: {delta}")
