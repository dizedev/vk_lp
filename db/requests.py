from typing import Optional

from loguru import logger
from sqlalchemy import select

import db


async def execute_statement(statement) -> None:
    """
    Возвращает результат выполнения statement
    :param statement:
    :return:
    """

    try:
        async with db.config.async_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        logger.exception(e)
        # return None


async def get_user_token(user_id: int) -> Optional[db.models.UsersTokens]:
    """
    Возвращает токен пользователя
    :param user_id: VKID
    """

    try:
        async with db.config.async_session() as session:
            result = await session.execute(select(db.models.UsersTokens).where(db.models.UsersTokens.vkid == user_id))
            return result.scalars().one_or_none()

    except Exception as e:
        logger.exception(e)
        return None


async def get_user_profile(user_id: int) -> Optional[db.models.UsersProfile]:
    """
    Получает профиль пользователя
    :param user_id: VKID
    """

    try:
        async with db.config.async_session() as session:
            result = await session.execute(select(db.models.UsersProfile).where(db.models.UsersProfile.vkid == user_id))
            return result.scalars().one_or_none()

    except Exception as e:
        logger.exception(e)
        return None
