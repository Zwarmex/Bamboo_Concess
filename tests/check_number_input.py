import unittest
from main_project.function_common import check_number_input


class TestCheckNumberInput(unittest.TestCase):

    def test_valid_input(self):
        self.assertTrue(check_number_input("123"), True)
        self.assertTrue(check_number_input("-123"), True)

    def test_invalid_input(self):
        self.assertFalse(check_number_input("123.45"), False)
        self.assertFalse(check_number_input("abc"), False)

    def test_minimum_only(self):
        self.assertFalse(check_number_input("", minimum=0), False)
        self.assertTrue(check_number_input("123", minimum=100), True)

    def test_maximum_only(self):
        self.assertFalse(check_number_input("123", maximum=100), False)

    def test_minimum_and_maximum(self):
        self.assertFalse(check_number_input("-123", minimum=-100, maximum=100), False)
        self.assertFalse(check_number_input("200", minimum=-100, maximum=100), False)


if __name__ == '__main__':
    unittest.main()
