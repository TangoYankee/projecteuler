"""
Problem #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from multiples_set import Set
from user_interface import UserInterface


def main():
    """
    user can input any natural number for the upper limit. 
    they can set the value and quantity of numbers from which they would like to find multiples
    """
    interface = UserInterface()
    interface.show_welcome()
    upper_limit = interface.get_upper_limit()
    if upper_limit == False:
        interface.show_tries_reached()
    else:
        numbers = interface.get_numbers(upper_limit)
        master_set = Set(numbers, upper_limit)
        multiples_sum = master_set.get_set_sum()
        interface.show_solution(multiples_sum)


if __name__ == "__main__":
    main()
