import git
import pytz
from vkbottle.user import Message, UserLabeler

from config import user, edit_message, prefix_bot
from custom_rules.permission import Permission
from utils import rewards

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about_cmd(ctx: Message):
    repo = git.Repo(search_parent_directories=True)
    version = repo.head.object.hexsha[:7]
    version_date = repo.head.object.committed_datetime.astimezone(pytz.timezone("Europe/Moscow"))

    await edit_message(ctx,
                       "Информация о боте 🤖:\n\n"
                       "Название бота 🤖: dize_lp\n"
                       f"Версия бота ⚙️: {version} от {version_date}\n"
                       "Создатель бота 👨‍🦱: @dize_dev (Илдырым Денница)\n"
                       f"Достижения🏆: {rewards['creator']}")

    await user.api.messages.send(
            peer_id=ctx.peer_id,
            random_id=0,
            attachment="photo-202995525_457239051"
    )
