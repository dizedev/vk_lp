import pytz
import git

from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot
from utils import rewards_list


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about(message: Message):
    repo = git.Repo(search_parent_directories=True)
    version = repo.head.object.hexsha[:7]
    version_date = repo.head.object.committed_datetime.astimezone(pytz.timezone("Europe/Moscow"))

    f'Текущая версия бота: {version} от {version_date}'

    await edit_message(message,
                       "Информация о боте 🤖:\n\n"
                       "Название бота 🤖: dize_lp\n"
                       f"Версия бота ⚙️: {version} от {version_date}\n"
                       "Создатель бота 👨‍🦱: @dize_dev (Илдырым Денница)\n"
                       f"Достижения🏆: {rewards_list[1]}")
