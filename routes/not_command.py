from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot


@bl.message(Permission(), text=prefix_bot + " <command>")
async def wrapper(message: Message):
    await edit_message(message, "Такой команды не существует")

