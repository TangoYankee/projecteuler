def find_master_multiples_set(all_multiples):
    """
    all multiples from every number consolidated into one set without duplicates
    """
    master_multiples = []
    for each_multiples in all_multiples:
        for multiple in each_multiples:
            if multiple not in master_multiples:
                master_multiples.append(multiple)
    return master_multiples


def find_all_multiples_sets(numbers, upper_limit):
    """
    collection of sets for the multiples of all numbers
    """
    all_multiples_sets = []
    for number in numbers:
        each_multiple_set = find_each_multiples_set(number, upper_limit)
        all_multiples_sets.append(each_multiple_set)
    return all_multiples_sets


def find_each_multiples_set(number, upper_limit):
    """
    the set of multiples generated from a single number
    """
    i = 1
    current_multiple = 0
    each_multiples = []
    while i < upper_limit:
        current_multiple = i * number
        if current_multiple < upper_limit:
            each_multiples.append(current_multiple)
            i += 1
        else:
            return each_multiples
