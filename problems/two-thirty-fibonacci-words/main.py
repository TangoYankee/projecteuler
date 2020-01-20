"""
Problem #230: Fibonacci Words

For any two strings of digits, A and B, we define FA,B to be the sequence (A,B,AB,BAB,ABBAB,...) in which each term is the concatenation of the previous two.
Further, we define DA,B(n) to be the nth digit in the first term of FA,B that contains at least n digits.

Example:
Let A=1415926535, B=8979323846. We wish to find DA,B(35), say.

The first few terms of FA,B are:
1415926535
8979323846
14159265358979323846
897932384614159265358979323846
14159265358979323846897932384614159265358979323846

Then DA,B(35) is the 35th digit in the fifth term, which is 9.

Now we use for A the first 100 digits of π behind the decimal point:

14159265358979323846264338327950288419716939937510
58209749445923078164062862089986280348253421170679

and for B the next hundred digits:

82148086513282306647093844609550582231725359408128
48111745028410270193852110555964462294895493038196 .

Find ∑n = 0,1,...,17   10n× DA,B((127+19n)×7n) .
"""

import math


class FibonacciWords:
    def __init__(self, A, B, to_n):
        self.terms = [A, B]
        self.term_length = len(A)
        self.to_n = to_n
        self.digits = []
        self._find_digits()

    def _find_digits(self):
        """
        use the golden ratio to determine which term contains the correct digit
        """
        for n in range(self.to_n, -1, -1):
            fibonacci_position = FibonacciPosition(n, self.term_length)
            digit = fibonacci_position.get_digit(self.terms)
            self.digits.append(digit)

    def get_digits_sum(self):
        return "".join(self.digits)


class FibonacciPosition:
    phi = 0.5 + math.sqrt(5) / 2

    def __init__(self, n, term_length):
        self.n = n
        self.term_length = term_length
        self.position = self._find_position()
        self.adjusted_position = self._shift_position()
        self.m = self.adjusted_position // (self.phi ** 2)
        self.x = math.ceil(self.m * self.phi ** 2)
        self.correct_term = self._find_correct_term()
        self.remainder_position = self._leftover_position()

    def get_digit(self, terms):
        return terms[self.correct_term][self.remainder_position]

    def _find_position(self):
        """
        generate a position for nth the character
        """
        return (127 + 19 * self.n) * (7 ** self.n) - 1

    def _shift_position(self):
        """
        adjust position to reflect each sequence only starts every 100th term
        """
        return self.position // self.term_length

    def _leftover_position(self):
        """
        take the remainder to know how deep into the term to go to find the digit
        """
        return self.position % self.term_length

    def _find_correct_term(self):
        """
        use either first or second term
        """
        if self.x == self.adjusted_position:
            return 0
        else:
            return 1


def main():
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    to_n = 17
    fibonacci_pi = FibonacciWords(A, B, to_n)
    print(fibonacci_pi.get_digits_sum())


if __name__ == "__main__":
    main()
