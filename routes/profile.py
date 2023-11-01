import git
from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot, prefix_dd
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " профиль"])
async def get_profile_cmd(message: Message):
    repo = git.Repo(search_parent_directories=True)
    version = repo.head.object.hexsha[:7]

    await edit_message(message,
                       f"[ Impulse LP ]\n"
                       f"Текущая версия: {version}\n"
                       f"Основной префикс: {prefix_bot}\n"
                       f"Префикс дд: {prefix_dd}"
    )
