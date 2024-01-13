import asyncio
import sys

from loguru import logger
from vkbottle.user import User

import config
import db

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")


async def main():
    from routes import labelers

    user_info = await db.requests.get_user_token()
    if not user_info:
        logger.error("user don't have a token in db!")
        return

    config.user = User(token=user_info.token)

    for custom_labeler in labelers:
        config.user.labeler.load(custom_labeler)

    loop.create_task(config.user.run_polling())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    loop.run_forever()
