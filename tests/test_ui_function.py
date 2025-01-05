import unittest
from tkinter import Tk
from main import window


class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.app = window

    def test_window_title(self):
        self.assertEqual(self.app.title(), "Password Generator")

    def test_entries_exist(self):
        website_entry = self.app.children['!entry']
        email_entry = self.app.children['!entry2']
        password_entry = self.app.children['!entry3']

        self.assertIsNotNone(website_entry)
        self.assertIsNotNone(email_entry)
        self.assertIsNotNone(password_entry)

    def test_generate_password_button(self):
        generate_button = self.app.children['!button']
        self.assertEqual(generate_button['text'], "Generate Password")

    def test_add_button(self):
        add_button = self.app.children['!button2']
        self.assertEqual(add_button['text'], "Add")


if __name__ == '__main__':
    unittest.main()
