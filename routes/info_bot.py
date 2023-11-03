import git
import pytz
from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " бот"])
async def about_cmd(ctx: Message):
    repo = git.Repo(search_parent_directories=True)
    version = repo.head.object.hexsha[:7]
    version_date = repo.head.object.committed_datetime.astimezone(pytz.timezone("Europe/Moscow"))

    # TODO: use Pillow to create img in real-time

    await edit_message(ctx, attachment="photo-202995525_457239051")
