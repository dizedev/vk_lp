from custom_rules.permission import Permission
from vkbottle.user import Message, UserLabeler
from config import edit_message, prefix_bot
from utils import rewards_list

listToStr = ' '.join(map(str, rewards_list))
bl = UserLabeler(custom_rules=Permission)


@bl.message(Permission(), text=[prefix_bot + " достижения"])
async def rewards(message: Message):
    await edit_message(message,
                       "Вот список всех достижений 🏆:\n " + listToStr)
