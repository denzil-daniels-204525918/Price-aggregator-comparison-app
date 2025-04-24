# src/main/module/saved_list.py

class SavedList:
    def __init__(self, saved_list_id: str, user_id: str, name: str, items: list[str]):
        self.id = saved_list_id
        self.user_id = user_id
        self.name = name
        self.items = items

    def __eq__(self, other):
        return (
                isinstance(other, SavedList)
                and self.id == other.id
                and self.user_id == other.user_id
                and self.name == other.name
                and self.items == other.items
        )

    def __repr__(self):
        return f"SavedList(id='{self.id}', user_id='{self.user_id}', name='{self.name}', items={self.items})"
