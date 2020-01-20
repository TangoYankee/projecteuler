import unittest

from main import FibonacciPosition


class TestFindPosition(unittest.TestCase):
    def test_find_position(self):
        """
        generate a position of nth the character
        """
        fibonacci_position = FibonacciPosition(2, 100)
        expected = 8085 - 1
        result = fibonacci_position._find_position()
        self.assertEqual(result, expected)


class TestShiftPosition(unittest.TestCase):
    def test_shift_position(self):
        """
        adjust position to reflect each sequence only starts every 100th term
        """
        fibonacci_position = FibonacciPosition(2, 100)
        expected = 80
        result = fibonacci_position._shift_position()
        self.assertEqual(result, expected)


class TestLeftoverPosition(unittest.TestCase):
    def test_leftover_position(self):
        """
        take the remainder to know how deep into the term to go to find the digit
        """
        fibonacci_position = FibonacciPosition(2, 100)
        expected = 84
        result = fibonacci_position._leftover_position()
        self.assertEqual(result, expected)
