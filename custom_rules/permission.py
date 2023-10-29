from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message
import json


def load_trusted_ids():
    try:
        with open("./user_ids.json", "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        # Если файл не существует, вернуть пустой список
        return []


class Permission(ABCRule[Message]):
    def __init__(self):
        self.trusted_ids = load_trusted_ids()

    async def check(self, event: Message) -> bool:
        return event.from_id in self.trusted_ids
