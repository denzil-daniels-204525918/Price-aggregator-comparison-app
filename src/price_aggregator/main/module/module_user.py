# src/main/user.py
class User:
    def __init__(self, user_id: str, name: str, email: str, password: str = ""):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password

    def __eq__(self, other):
        return (
                isinstance(other, User)
                and self.id == other.id
                and self.name == other.name
                and self.email == other.email
        )

    def __repr__(self):
        return f"User(id='{self.id}', name='{self.name}', email='{self.email}')"