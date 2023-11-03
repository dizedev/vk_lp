import git
from vkbottle.user import Message, UserLabeler

import db.requests
from config import edit_message, prefix_bot, prefix_dd
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " профиль"])
async def get_profile_cmd(ctx: Message):
    repo = git.Repo(search_parent_directories=True)
    version = repo.head.object.hexsha[:7]
    info = await db.requests.get_user_profile(user_id=ctx.from_id)

    await edit_message(ctx,
                       f"[ Impulse LP ]\n"
                       f"Текущая версия: {version}\n"
                       f"Основной префикс: {info.prefix}\n"
                       f"Префикс дд: {info.prefix_delete}\n"
                       f"{info.prefix_d}\n"
                       f"\nДостижения\n"
                       f"{info.achievements}\n"
                       f"Последний вход на сайт: {info.last_login}\n"
                       f"Довы:\n"
                       f"{info.trusted_ids}"
                       )
