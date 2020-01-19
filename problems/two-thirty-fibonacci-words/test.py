import unittest

from main import (
    # find_highest_position,
    # find_position,
    # find_positions,
    generate_sequence,
    find_digit,
    find_term_indices,
    find_digits_by_tens,
)

from positions import (
    find_highest_position,
    find_position,
    find_positions,
)


class TestFindPosition(unittest.TestCase):
    def test_find_position(self):
        """
        generate a position of nth the character
        """
        n = 2
        expected = 8085
        result = find_position(n)
        self.assertEqual(result, expected)


class TestFindPositions(unittest.TestCase):
    def test_find_positions(self):
        """
        generate a position of nth the character
        """
        to_n = 2
        expected = [127, 1022, 8085]
        result = find_positions(to_n)
        self.assertEqual(result, expected)


class TestFindHighestPosition(unittest.TestCase):
    def test_find_highest_position(self):
        """
        the positions are presorted to have the highest at the end
        """
        positions = [127, 1022, 8085]
        expected = 8085
        result = find_highest_position(positions)
        self.assertEqual(result, expected)


class TestFindHighestPosition(unittest.TestCase):
    def test_generate_sequence(self):
        """
        the positions are presorted to have the highest at the end
        """
        F = [1, 1]
        highest_position = 10
        result = generate_sequence(F, highest_position)
        expected = [1, 1, 2, 3, 5, 8, 13]
        self.assertEqual(result, expected)


class TestFindDigit(unittest.TestCase):
    def test_find_digit(self):
        """
        get the digit from the term based on the position
        """
        term = "ABCDE"
        position = 3
        result = find_digit(term, position)
        expected = "C"
        self.assertEqual(result, expected)


class TestFindDigits(unittest.TestCase):
    def test_find_indices(self):
        """
        collect the digits for all of the positions
        """
        positions = [200, 400, 1000]
        F = [100, 100, 200, 300, 500, 800, 1300]
        expected = [2, 4, 6]
        result = find_term_indices(positions, F)
        self.assertEqual(result, expected)


class TestFindDigitsByTens(unittest.TestCase):
    def test_find_digits_by_tens(self):
        """
        digits multiplied by ten raised to the power of n
        """
        digits = ["1", "2", "3", "4"]
        expected = [1, 20, 300, 4000]
        result = find_digits_by_tens(digits)
        self.assertEqual(result, expected)
