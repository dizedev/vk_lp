import sys
from config import user
from routes import labelers
from loguru import logger


logger.add(sys.stderr, format="{time} {level} {message}", filter="my_module", level="INFO")

for custom_labeler in labelers:
    user.labeler.load(custom_labeler)

if __name__ == "__main__":
    user.run_forever()
