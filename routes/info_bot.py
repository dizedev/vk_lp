from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot
from utils import rewards_list


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about_bot(message: Message):
    await edit_message(message,
                       f"Информация о боте 🤖:\n\n Название бота 🤖: dize_lp\n Версия бота ⚙️: v0.1\n Создатель бота 👨‍🦱: @dize_dev(Илдырым Денница)\n Достижения🏆: {rewards_list[1]}")
