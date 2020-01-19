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


def main():
    """
    the summation of the nth position of a concatentated string as n goes from 0 to 17
    """
    A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
    B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
    to_n = 17

    positions = find_positions(to_n)
    # adjusted_positions = map(lambda x: x/100 positions)
    highest_position = find_highest_position(positions)
    F = [100, 100]
    F = generate_sequence(F, highest_position)
    # print(f'number of terms: {len(F)}\nsecond highest term: {F[-2]}\nhighest position {highest_position}')
    term_indices = find_term_indices(positions, F)

    # digits = find_digits(positions, F)
    # digits_by_tens = find_digits_by_tens(digits)
    # print(sum(digits_by_tens))


def find_term_indices(positions, F):
    """
    collect the indices of the terms that satisfy all of the positions generated from 0 to 17
    """
    term_indices = []
    for position in positions:
        # print(f'length of F: {len(F)}')
        term_index = 0
        for i in range(term_index, (len(F)+1)):
            term = F[i]
            if term >= position:
                term_index = F.index(term)
                # print(f'index for term: {term_index}')
                term_indices.append(term_index)
                break
    return term_indices


def find_digit(term, position):
    """
    get the digit from the term based on the position
    """
    return term[position - 1 : position]


def find_digits_by_tens(digits):
    """
    ten raised to the power of n
    """
    digits_by_tens = []
    n = 0
    for digit in digits:
        tens = 10 ** n
        real_digit = int(digit)
        digit_by_ten = real_digit * tens
        digits_by_tens.append(digit_by_ten)
        n += 1
    return digits_by_tens


# def cut_f(F, term):
#     """
#     Reduce the number of elements that need to be searched
#     """
#     term_position = F.index(term)
#     return F[term_position + 1 :]



def generate_sequence(F, highest_position):
    """
    concatenate and save the strings until they are long enough to satisfy all positions
    """
    current = F[-1]
    while current < highest_position:
        current = F[-2]+F[-1]
        F.append(current)
    return F


def find_highest_position(positions):
    """
    positions are presorted to have the highest at the end
    """
    return positions[-1]


def find_positions(to_n):
    positions = []
    for n in range(to_n + 1):
        position = find_position(n)
        positions.append(position)
    return positions


def find_position(n):
    """
    generate a position for nth the character
    """
    return (127 + 19 * n) * (7 ** n)


# def concat_string(minus_two, minus_one):
#     """
#     concat previous two strings
#     """
#     return minus_two + minus_one


if __name__ == "__main__":
    main()
