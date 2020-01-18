import unittest

from main import find_position, concat_string, find_tens


class TestFindPosition(unittest.TestCase):
    def test_find_position(self):
        """
        generate a position of nth the character
        """
        n = 2
        expected = 8085
        result = find_position(n)
        self.assertEqual(result, expected)


class TestConcatString(unittest.TestCase):
    def test_concat_string(self):
        """
        generate a position of nth the character
        """
        minus_two = "A"
        minus_one = "B"
        expected = "AB"
        result = concat_string(minus_two, minus_one)
        self.assertEqual(result, expected)


class TestTens(unittest.TestCase):
    def test_tens(self):
        """
        generate a position of nth the character
        """
        n = 2
        expected = 100
        result = find_tens(n)
        self.assertEqual(result, expected)

class TestFindPositions(unittest.TestCase):
    def test_find_positions(self):
        """
        generate a position of nth the character
        """
        to_n = 2
        expected = [8085]
        result = find_position(n)
        self.assertEqual(result, expected)
