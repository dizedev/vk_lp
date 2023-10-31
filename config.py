from vkbottle.user import Message

TOKEN = "test"
prefix_bot = "хуй"
prefix_dd = "дд"
user = None

DB_LOGIN = "postgres"
DB_PASSWORD = "MQLDUhDrF3cxj3zszsA63tZoSeSW"
DB_HOST = "51.38.114.136"
DB_NAME = "vk_lp"


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
