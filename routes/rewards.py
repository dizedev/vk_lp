from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message,  prefix_bot
from utils import rewards_list

listToStr = ' '.join(map(str, rewards_list))


@bl.message(Permission(), text=[prefix_bot + " достижения"])
async def rewards(message: Message):
    await edit_message(message,
                       "Вот список всех достижений 🏆:\n " + listToStr)
