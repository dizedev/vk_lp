from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message


@bl.message(Permission(), text="хелло")
async def hello(message: Message):
    await edit_message(
        message,
        "привет"
    )
