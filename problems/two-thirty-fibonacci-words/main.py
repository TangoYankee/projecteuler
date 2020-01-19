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


def main():
    """
    use the golden ratio to determine which term the digit will fall into
    """
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    terms = [A, B]
    phi = 0.5 + math.sqrt(5) / 2
    to_n = 17

    digits = []
    for n in range(to_n, -1, -1):
        position = find_position(n)
        adjusted_position = shift_position(position, terms)
        remainder_position = leftover_position(position, terms)
        m = adjusted_position // (phi ** 2)
        x = math.ceil(m * phi ** 2)
        correct_term = find_correct_term(x, adjusted_position)
        digit = terms[correct_term][remainder_position]
        digits.append(digit)
    solution = "".join(digits)
    print(f"solution: {solution}")


def find_correct_term(x, adjusted_position):
    """
    use either first or second term
    """
    if x == adjusted_position:
        return 0
    else:
        return 1


def find_position(n):
    """
    generate a position for nth the character
    """
    return (127 + 19 * n) * (7 ** n) - 1


def shift_position(position, terms):
    """
    adjust position to reflect each sequence only starts every 100th term
    """
    return position // len(terms[0])


def leftover_position(position, terms):
    """
    take the remainder to know how deep into the term to go to find the digit
    """
    return position % len(terms[0])


if __name__ == "__main__":
    main()
