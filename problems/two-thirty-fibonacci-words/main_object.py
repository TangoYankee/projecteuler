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
    phi = 0.5 + math.sqrt(5) / 2

    def __init__(self, A, B, to_n):
        self.terms = [A, B]
        self.to_n = to_n
        self.digits = []
        self._find_digits()

    def _find_digits(self):
        for n in range(self.to_n, -1, -1):
            position = self._find_position(n)
            adjusted_position = self._shift_position(position)
            remainder_position = self._leftover_position(position)
            m = adjusted_position // (self.phi ** 2)
            x = math.ceil(m * self.phi ** 2)
            correct_term = self._find_correct_term(x, adjusted_position)
            digit = self.terms[correct_term][remainder_position]
            self.digits.append(digit)

    def _find_position(self, n):
        """
        generate a position for nth the character
        """
        return (127 + 19 * n) * (7 ** n) - 1

    def _shift_position(self, position):
        """
        adjust position to reflect each sequence only starts every 100th term
        """
        return position // len(self.terms[0])

    def _leftover_position(self, position):
        """
        take the remainder to know how deep into the term to go to find the digit
        """
        return position % len(self.terms[0])

    def _find_correct_term(self, x, adjusted_position):
        """
        use either first or second term
        """
        if x == adjusted_position:
            return 0
        else:
            return 1

    def get_digits_sum(self):
        return "".join(self.digits)


def main():
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    to_n = 17
    fibonacci_pi = FibonacciWords(A, B, to_n)
    print(fibonacci_pi.get_digits_sum())


if __name__ == "__main__":
    main()
