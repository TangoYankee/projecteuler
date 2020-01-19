import unittest

from main import (
    find_highest_position,
    find_position,
    find_positions,
    concat_string,
    generate_sequence,
    find_digit,
    cut_f,
    find_digits,
    find_digits_by_tens,
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
        F = ["A", "B"]
        highest_position = 10
        result = generate_sequence(F, highest_position)
        expected = ["A", "B", "AB", "BAB", "ABBAB", "BABABBAB", "ABBABBABABBAB"]
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


class TestCutF(unittest.TestCase):
    def test_cut_F(self):
        """
        Reduce the number of elements that need to be searched
        """
        term = "BAB"
        F = ["A", "B", "AB", "BAB", "ABBAB", "BABABBAB", "ABBABBABABBAB"]
        expected = ["ABBAB", "BABABBAB", "ABBABBABABBAB"]
        result = cut_f(F, term)
        self.assertEqual(result, expected)


class TestFindDigits(unittest.TestCase):
    def test_find_digits(self):
        """
        collect the digits for all of the positions
        """
        positions = [2, 4, 10]
        F = ["A", "B", "AB", "BAB", "ABBAB", "BABABBAB", "ABBABBABABBAB"]
        expected = ["B", "A", "B"]
        result = find_digits(positions, F)
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
