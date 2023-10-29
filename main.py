import sys
import asyncio
from config import user
from routes import labelers
from loguru import logger

logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

for custom_labeler in labelers:
    user.labeler.load(custom_labeler)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(user.run_polling())
    loop.run_forever()
