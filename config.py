from vkbottle.user import UserLabeler, Message, User

TOKEN = 'vk1.a.4nNdLuOJin9tn71J-cKGu6MKCR2rNHkdRPn4lbW28CS9aL0Q-rhG3ZQi6UQnV9ClpBrNp2obRUltWREoSuwz2Km7OXGlBaP3jt9KsEeut4N3OvHWoTUuqNEtiRrgz2koSrPXLEJZ8i974KD2CgXWqmX4IsSC3kCMDK_aS1xetU3S38-Z1JFyNZu5Tl8yUGopptCjEqA9jF8CjznWv1gC2A'

bl = UserLabeler()

user = User(token=TOKEN)


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
