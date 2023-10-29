from vkbottle.dispatch.rules import ABCRule
from vkbottle.user import Message
import json



class Permission(ABCRule[Message]):
    def __init__(self):
        self.trusted_ids = self.load_trusted_ids()

    def load_trusted_ids(self):
        try:
            with open("./user_ids.json", "r") as json_file:
                data = json.load(json_file)
                return data
        except FileNotFoundError:
            # Если файл не существует, вернуть пустой список
            return []

    async def check(self, event: Message) -> bool:
        return event.from_id in self.trusted_ids


