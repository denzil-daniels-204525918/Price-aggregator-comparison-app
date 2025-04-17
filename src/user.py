# src/user.py

class User:
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.logged_in = False

    def login(self):
        # Simulate login process
        self.logged_in = True
        print(f"{self.name} has logged in.")

    def logout(self):
        self.logged_in = False
        print(f"{self.name} has logged out.")

    def __str__(self):
        return f"User({self.user_id}, {self.name}, {self.email})"
