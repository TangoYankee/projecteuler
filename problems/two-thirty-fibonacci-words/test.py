import unittest

from main import find_position, shift_position, leftover_position


class TestFindPosition(unittest.TestCase):
    def test_find_position(self):
        """
        generate a position of nth the character
        """
        n = 2
        expected = 8085 - 1
        result = find_position(n)
        self.assertEqual(result, expected)


class TestShiftPosition(unittest.TestCase):
    def test_shift_position(self):
        """
        adjust position to reflect each sequence only starts every 100th term
        """
        A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
        terms = [A, B]
        value = 150
        expected = 1
        result = shift_position(value, terms)
        self.assertEqual(result, expected)


class TestLeftoverPosition(unittest.TestCase):
    def test_leftover_position(self):
        """
        take the remainder to know how deep into the term to go to find the digit
        """
        A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
        terms = [A, B]
        value = 150
        expected = 50
        result = leftover_position(value, terms)
        self.assertEqual(result, expected)
