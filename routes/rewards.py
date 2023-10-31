from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot
from custom_rules.permission import Permission
import utils


bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " достижения"])
async def rewards_cmd(message: Message):
    await edit_message(message,
                       f"Вот список всех достижений 🏆:\n{utils.next_line_symbol.join(utils.rewards)}")
