import unittest
from password_generator import password_generator


class TestPasswordGenerator(unittest.TestCase):
    def test_password_length(self):
        password = password_generator(15, 3, 4)
        self.assertEqual(len(password), 22)

    def test_password_contains_letters(self):
        password = password_generator(15, 0, 0)
        self.assertTrue(any(char.isalpha() for char in password))

    def test_password_contains_symbols(self):
        password = password_generator(0, 3, 0)
        self.assertTrue(any(char in "!#$%&()*+" for char in password))

    def test_password_contains_numbers(self):
        password = password_generator(0, 0, 4)
        self.assertTrue(any(char.isdigit() for char in password))


if __name__ == '__main__':
    unittest.main()
