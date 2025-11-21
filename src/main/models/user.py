# --- src/main/models/user.py ---
class User:
    def __init__(self, user_id: str, name: str, email: str, password: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self._password = password
        self._is_logged_in = False

    def login(self, password: str) -> bool:
        if password == self._password:
            self._is_logged_in = True
            print(f"{self.name} logged in.")
            return True
        print("Incorrect password.")
        return False

    def logout(self) -> bool:
        self._is_logged_in = False
        print(f"{self.name} logged out.")
        return True