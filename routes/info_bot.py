from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot, user


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about_bot(message: Message):
    peer_id = message.peer_id

    # await edit_message(message,
    #                    f"Информация о боте 🤖:\n\n Название бота 🤖: Impulse LP\n c\n Создатель бота 👨‍🦱: @dize_dev(Илдырым Денница)\n Достижения🏆: {rewards_list[1]}")
    # await asyncio.sleep(0.5)
    await edit_message(
        message,
        " ")

    await user.api.messages.send(
        peer_id=peer_id,
        random_id=0,
        attachment="photo-202995525_457239051"


    )
