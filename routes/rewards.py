from vkbottle.user import Message, UserLabeler

import db
import utils
from config import edit_message, prefix_bot
from custom_rules.permission import Permission

listToStr = ' '.join(map(str, rewards_list))


@bl.message(Permission(), text=[prefix_bot + " достижения"])
async def rewards_cmd(ctx: Message):
    text = "Список всех достижений:\n\n"
    have_ = ""
    dont_have = ""
    info = await db.requests.get_user_profile(user_id=ctx.from_id)

    # TODO: CHECK BEFORE DEPLOY!!
    # TODO: create table in db
    # TODO: fill items in models.py

    for item in info.achievements:
        if item in utils.rewards.keys():
            have_ += f"{utils.rewards[item]}\n"
        else:
            dont_have += f"{utils.rewards[item]}\n"

    if have_ != "":
        text += "Открытые:\n"
        text += have_

    if dont_have != "":
        text += "Неоткрытые:\n"
        text += dont_have

    await edit_message(ctx, text)
