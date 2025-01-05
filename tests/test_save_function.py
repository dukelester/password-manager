import unittest
import os
import json
from main import save


class MockEntry:
    """A simple mock for tkinter Entry widget."""
    def __init__(self, text):
        self.text = text

    def get(self):
        return self.text

    def delete(self, start, end):
        self.text = ""


class TestSaveFunction(unittest.TestCase):
    def setUp(self):
        # Set up mock entries
        self.website_entry = MockEntry("example.com")
        self.email_entry = MockEntry("user@example.com")
        self.password_entry = MockEntry("password123")

        # Create a temporary data file
        self.data_file = "test_data.json"
        with open(self.data_file, "w") as f:
            json.dump({}, f)

    def tearDown(self):
        os.remove(self.data_file)

    def test_save_valid_data(self):
        save_data = {
            "website_entry": self.website_entry,
            "email_entry": self.email_entry,
            "password_entry": self.password_entry
        }
        save(**save_data)

        with open(self.data_file, "r") as f:
            data = json.load(f)

        self.assertIn("example.com", data)
        self.assertEqual(data["example.com"]["email"], "user@example.com")
        self.assertEqual(data["example.com"]["password"], "password123")

    def test_save_empty_fields(self):
        self.website_entry.text = ""
        with self.assertRaises(SystemExit):
            save(
                website_entry=self.website_entry,
                email_entry=self.email_entry,
                password_entry=self.password_entry
            )


if __name__ == '__main__':
    unittest.main()
