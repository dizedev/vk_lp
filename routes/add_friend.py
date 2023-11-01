from vkbottle import VKAPIError
from vkbottle.user import Message, UserLabeler

from config import edit_message, prefix_bot, user
from custom_rules.permission import Permission

bl = UserLabeler()


@bl.message(Permission(), text=[prefix_bot + " +др"])
async def add_to_friends_cmd(ctx: Message):
    if not ctx.reply_message:
        await ctx.answer("❗ Ошибка при выполнении, необходимо пересланное сообщение")
        return

    friend_id = ctx.reply_message.from_id

    try:
        await user.api.friends.add(user_id=friend_id)
        await edit_message(ctx, "✅ Все отлично, запрос отправлен")
    except Exception as e:
        if VKAPIError[174]:
            await edit_message(ctx, "❗ Невозможно добавить в друзья самого себя")
        elif VKAPIError[175]:
            await edit_message(ctx,
                               "❗ Невозможно добавить в друзья пользователя, который занес Вас в свой черный список")
        elif VKAPIError[176]:
            await edit_message(ctx,
                               "❗ Невозможно добавить в друзья пользователя, который занесен в Ваш черный список")
        else:
            await edit_message(ctx, f"❗ Невозможно добавить в друзья пользователя: {e.message}")


@bl.message(Permission(), text=[prefix_bot + " -др"])
async def remove_from_friends_cmd(ctx: Message):
    if not ctx.reply_message:
        await edit_message(ctx, "❗ Ошибка при выполнении, необходимо пересланное сообщение")
        return

    friend_id = ctx.reply_message.from_id
    response = await user.api.friends.delete(user_id=friend_id)

    if not response.success:
        await edit_message(ctx, "❗ Произошла ошибка при удалении друга")
        return

    if response.friend_deleted:
        await edit_message(ctx, "✅ Друг удален")
    elif response.out_request_deleted:
        await edit_message(ctx, "✅ Отменена исходящая заявка")
    elif response.in_request_deleted:
        await edit_message(ctx, "✅ Отклонена входящая заявка")
    elif response.suggestion_deleted:
        await edit_message(ctx, "✅ Отклонена рекомендация друга")
    else:
        await edit_message(ctx, "❗ Произошла ошибка")
