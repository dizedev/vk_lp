from custom_rules.permission import Permission
from vkbottle.user import Message
from config import bl, edit_message, prefix_bot, user


@bl.message(Permission(), text=[prefix_bot + " +др"])
async def add_to_fr(message: Message):
    if not message.reply_message:
        await message.answer("❗ Ошибка при выполнении, необходимо пересланное сообщение")
        return

    friend_id = message.reply_message.from_id
    try:
        await user.api.friends.add(user_id=friend_id)
        await edit_message(message, "✅ Все отлично, запрос отправлен")
    except Exception as e:
        if e.code == 174:
            await edit_message(message, "❗ Невозможно добавить в друзья самого себя")
        elif e.code == 175:
            await edit_message(message, "❗ Невозможно добавить в друзья пользователя, который занес Вас в свой черный список")
        elif e.code == 176:
            await edit_message(message, "❗ Невозможно добавить в друзья пользователя, который занесен в Ваш черный список")
        else:
            await edit_message(message, f"❗ Невозможно добавить в друзья пользователя: {e.message}")


@bl.message(Permission(), text=[prefix_bot + " -др"])
async def remove_from_fr(message: Message):
    if not message.reply_message:
        await edit_message(message, "❗ Ошибка при выполнении, необходимо пересланное сообщение")
        return

    friend_id = message.reply_message.from_id

    response = await user.api.friends.delete(user_id=friend_id)
    if response.success:
        if response.friend_deleted:
            await edit_message(message, "✅ Друг удален")
        elif response.out_request_deleted:
            await edit_message(message, "✅ Отменена исходящая заявка")
        elif response.in_request_deleted:
            await edit_message(message, "✅ Отклонена входящая заявка")
        elif response.suggestion_deleted:
            await edit_message(message, "✅ Отклонена рекомендация друга")
        else:
            await edit_message(message, "❗ Произошла ошибка")
    else:
        await edit_message(message, "❗ Произошла ошибка при удалении друга")
