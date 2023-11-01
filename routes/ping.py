from vkbottle.user import Message, UserLabeler

import utils
from config import edit_message, prefix_bot
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " пинг"])
async def ping_cmd(ctx: Message):
    await edit_message(
            ctx,
            await utils.ping(ctx, "ПОНГ")
    )
