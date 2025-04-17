import unittest
from src.user import User

class TestUser(unittest.TestCase):
    def test_user_creation(self):
        user = User(user_id="1", name="John Doe", email="john.doe@example.com", password="password123")
        self.assertEqual(user.user_id, "1")
        self.assertEqual(user.name, "John Doe")
        self.assertEqual(user.email, "john.doe@example.com")

    def test_login(self):
        user = User(user_id="1", name="John Doe", email="john.doe@example.com", password="password123")
        self.assertTrue(user.login("password123"))
        self.assertFalse(user.login("wrongpassword"))

    def test_logout(self):
        user = User(user_id="1", name="John Doe", email="john.doe@example.com", password="password123")
        user.login("password123")
        self.assertTrue(user.logout())

if __name__ == '__main__':
    unittest.main()
