import uuid
from dataclasses import dataclass
from typing import List


@dataclass
class TodoItem:
    id: uuid.UUID
    value: str


class DBHandler:
    todo_items: List[TodoItem]

    def __init__(self):
        self.todo_items = [
            TodoItem(
                id=uuid.uuid4(),
                value="Buy a new gaming pc",
            ),
            TodoItem(
                id=uuid.uuid4(),
                value="Have fun",
            ),
        ]

    def get_todo_items(self):
        return self.todo_items

    def add_todo_item(self, value: str):
        self.todo_items.insert(
            0,
            TodoItem(
                id=uuid.uuid4(),
                value=value,
            ),
        )

    def clear_todo_items(self):
        self.todo_items = []

    def remove_todo_item(self, item_id: str):
        self.todo_items = [item for item in self.todo_items if not str(item.id) == item_id]


db_handler = DBHandler()
