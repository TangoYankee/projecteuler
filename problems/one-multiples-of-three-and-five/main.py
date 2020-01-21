"""
Problem #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""


from user_interface import welcome, find_numbers, find_upper_limit
# from multiples import find_all_multiples_sets, find_master_multiples_set
from multiples_set import Set


def main():
    """
    user can input any natural number for the upper limit. 
    they can set the value and quantity of numbers from which they would like to find multiples
    """
    welcome()
    upper_limit = find_upper_limit()
    numbers = find_numbers(upper_limit)
    # all_multiples_sets = find_all_multiples_sets(numbers, upper_limit)
    # master_multiples_set = find_master_multiples_set(all_multiples_sets)
    # sum_master_multiples = sum(master_multiples_set)
    multiples_set = Set(numbers, upper_limit)
    print(multiples_set.get_set_sum())


if __name__ == "__main__":
    main()
