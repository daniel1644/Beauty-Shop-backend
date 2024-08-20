# tests/unit/test_models.py
import unittest
from app.models import User

class TestUserModel(unittest.TestCase):
    def test_user_creation(self):
        user = User(username="testuser", email="test@example.com", password="password")
        self.assertEqual(user.username, "testuser")
