import datetime
from custom_rules.permission import Permission
from vkbottle.user import Message, UserLabeler
from config import user, prefix_dd

bl = UserLabeler(custom_rules=Permission)
DD_SCRIPT = (
    'var i = 0;var msg_ids = [];var count = %d;'
    'var items = API.messages.getHistory({"peer_id":%d,"count":"200", "offset":"0"}).items;'
    'while (count > 0 && i < items.length) {if (items[i].out == 1) {if (items[i].id == %d) {'
    'if (items[i].reply_message) {msg_ids.push(items[i].id);msg_ids.push(items[i].reply_message.id);'
    'count = 0;};if (items[i].fwd_messages) {msg_ids.push(items[i].id);var j = 0;while (j < '
    'items[i].fwd_messages.length) {msg_ids.push(items[i].fwd_messages[j].id);j = j + 1;};count = 0;};};'
    'msg_ids.push(items[i].id);count = count - 1;};if ((%d - items[i].date) > 86400) {count = 0;};i = i + 1;};'
    'API.messages.delete({"message_ids": msg_ids});return count;'
)


@bl.message(
        Permission(),
        text=[prefix_dd + " <count:int>"],
)
async def dd_handler(message: Message, count: int = 2):
    await user.api.execute(
            DD_SCRIPT % (
                count,
                message.peer_id,
                message.from_id,
                int(datetime.datetime.now().timestamp())
            )
    )


@bl.message(
        Permission(),
        text=["все", "всё"],
)
async def dd_all_handler(message: Message):
    count = 1000

    await user.api.execute(
            DD_SCRIPT % (
                count,
                message.peer_id,
                message.from_id,
                int(datetime.datetime.now().timestamp())
            )
    )
