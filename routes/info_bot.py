from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message


@bl.message(Permission(), text="бот")
async def hello(message: Message):
    await edit_message(
        message,
        "Информация о боте 🤖:\n\n Название бота 🤖: dize_lp\n Версия бота ⚙️: v0.1\n Создатель бота 👨‍🦱: @dize_dev(Илдырым Денница)."
    )
