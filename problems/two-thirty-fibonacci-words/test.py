import unittest

from main import (
    # find_highest_position,
    # find_position,
    # find_positions,
    generate_sequence,
    find_digit,
    find_term_indices,
    find_digits_by_tens,
    shift_position,
    leftover_position
)

from positions import (
    find_highest_position,
    find_position,
    find_positions,
)

from predict_term import predict_term, is_even

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

class TestIsEven(unittest.TestCase):
    '''
    algorithms for the next term are based on whether it is an even or odd index
    '''
    def test_is_even(self):
        value = 4
        result = is_even(value)
        self.assertTrue(result)

    def test_is_odd(self):
        value = 5
        result = is_even(value)
        self.assertFalse(result)


# class TestPredictTerm(unittest.TestCase):
#     # ['A', 'B', 'AB', 'BAB', 'ABBAB', 'BABABBAB', 'ABBABBABABBAB', 'BABABBABABBABBABABBAB', 'ABBABBABABBABBABABBABABBABBABABBAB', 'BABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBAB', 'ABBABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBAB', 'BABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBAB']
#     def test_predict_odd_term(self):
#         '''
#         ability to predicted which term will appear at a given index of the sequence
#         '''
#         index = 11
#         expected = 'BABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBABABBABBABABBABBABABBABABBABBABABBAB'
#         result = predict_term(index)
#         self.assertEqual(result, expected)



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
