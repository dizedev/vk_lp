from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=prefix_bot + " <command>")
async def wrapper(message: Message):
    await edit_message(message, "Такой команды не существует")
