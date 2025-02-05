import unittest
from authentication import database, password_strength


class TestAuthentication(unittest.TestCase):

    def test_database_valid_user(self):
        self.assertTrue(database("tstark", "password"))

    def test_database_invalid_user(self):
        self.assertFalse(database("nonexistent", "SomePassword"))

    def test_database_wrong_password(self):
        self.assertFalse(database("tstark", "WrongPass"))

    def test_password_strength_min_length(self):
        self.assertFalse(password_strength("Aa1!"))

    def test_password_strength_max_length(self):
        self.assertFalse(password_strength("A" * 51 + "1!"))

    def test_password_strength_no_special_char(self):
        self.assertFalse(password_strength("Password123"))

    def test_password_strength_no_digit(self):
        self.assertFalse(password_strength("Password!@#"))

    def test_password_strength_no_uppercase(self):
        self.assertFalse(password_strength("password1!"))

    def test_password_strength_no_lowercase(self):
        self.assertFalse(password_strength("PASSWORD1!"))

    def test_password_strength_valid(self):
        self.assertTrue(password_strength("Valid1!@"))


if __name__ == "__main__":
    unittest.main()
