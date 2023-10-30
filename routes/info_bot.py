import asyncio

from custom_rules.permission import Permission
from vkbottle.user import Message
from vkbottle.dispatch.views.abc.message import bl, edit_message, prefix_bot, user
from utils import rewards_list


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about_bot(message: Message):
    peer_id = message.peer_id

    await edit_message(message,
                       f"Информация о боте 🤖:\n\n Название бота 🤖: Impulse LP\n Версия бота ⚙️: v0.1\n Создатель бота 👨‍🦱: @dize_dev(Илдырым Денница)\n Достижения🏆: {rewards_list[1]}")
    await asyncio.sleep(0.5)

    await user.api.messages.send(
        peer_id=peer_id,
        random_id=0,
        sticker_id=79157,

    )
