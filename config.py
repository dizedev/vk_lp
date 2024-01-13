import vkbottle
from vkbottle.user import Message
import typing

TOKEN = "test"
prefix_bot = "хуй"
prefix_dd = "дд"
user: typing.Optional[vkbottle.User] = None

DB_LOGIN = ""
DB_PASSWORD = ""
DB_HOST = ""
DB_NAME = ""


async def edit_message(
        message: Message,
        text: str = '',
        **kwargs
) -> int:
    kwargs.setdefault('message_id', message.id)
    kwargs.setdefault('message', text)
    kwargs.setdefault('peer_id', message.peer_id)
    kwargs.setdefault('keep_forward_messages', True)
    kwargs.setdefault('keep_snippets', True)
    kwargs.setdefault('dont_parse_links', False)

    return await user.api.messages.edit(
            **kwargs
    )
