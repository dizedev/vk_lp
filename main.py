import asyncio
import sys
from vkbottle.user import User
import db.requests
from routes import labelers
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")
user = None


async def main():
    global user

    token = await db.requests.get_user_token(1232131)
    user = User(token=token)

    for custom_labeler in labelers:
        user.labeler.load(custom_labeler)

    user.run_forever()


if __name__ == "__main__":
    asyncio.run(main())
