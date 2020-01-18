"""
Problem #1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
# requirements

# Get a user inputs. (On reject, ask again. On success, return value. Always offer to quit)
# - upper limit (Natural number greater than/equal to 2.) (Test=reject and ask again)
# - multiples until they no longer want to enter them
    # - cannot repeat multiples
    # - cannot be higher than upper limit

# Create a list of lists to hold the multiples for each number
# - for each number, list all of the multiples underneath the upper limit

# List the multiples underneath the upper limit
# - for each number less than the upper limit, multiply it by the multiple until it hits the upper limit
# - add the multiple to the list

# Find the sum of all numbers in the list of lists/array

# output the result to the console

def main():
    print("Welcome! We will find the sum of all the multiples of numbers you select which are below an upper limit you set")
    upper_limit = set_upper_limit()
    numbers = set_numbers(upper_limit)
    all_multiples = set_all_multiples(numbers, upper_limit)
    master_multiples = consolidate_multiples(all_multiples)
    sum_all_multiples = sum(master_multiples)
    print(sum_all_multiples)

def consolidate_multiples(all_multiples):
    master_multiples = []
    for each_multiples in all_multiples:
        for multiple in each_multiples:
            if multiple not in master_multiples:
                master_multiples.append(multiple)
    return master_multiples

def set_sum_all_multiples(all_multiples):
    sum_all_multiples = 0
    for each_multiples in all_multiples:
        sum_all_multiples += sum(each_multiples)
    return sum_all_multiples

def set_all_multiples(numbers, upper_limit):
    all_multiples = []
    for number in numbers:
        each_multiples = set_each_multiples(number, upper_limit)
        all_multiples.append(each_multiples)
    return all_multiples

def set_each_multiples(number, upper_limit):
    i = 1
    current_multiple = 0
    each_multiples = []
    while (i < upper_limit):
        current_multiple = i*number
        if current_multiple < upper_limit:
            each_multiples.append(current_multiple)
            i+=1
        else:    
            return each_multiples

def set_numbers(upper_limit):
    numbers = []
    enter_more = 'y'
    while (enter_more == 'y') & (len(numbers) < upper_limit ):
        number = input("Please input a number: ")
        number = to_int(number)
        if is_int(number):
            if (number < upper_limit) & (number not in numbers):
                numbers.append(number)
            else:
                print("This value is not below the upper limit or has already been used")
        else:
            print("This value is not an integer")
        if len(numbers) == 0:
            continue
        else:
            enter_more = input("To input more numbers, enter 'y'. Press any other key to continue: ")
    return numbers

def set_upper_limit():
    upper_limit_floor = 2
    tries = 0
    while tries < 2:
        upper_limit = input("Please enter your upper limit: ")
        upper_limit = to_int(upper_limit)
        if is_int(upper_limit):
            if (upper_limit >= upper_limit_floor):
                return upper_limit
            else:
                print("This integer is not at least 2")
        else:
            print("This is not an integer")
        tries += 1
    return ("No correct upper limit entered")

def to_int(raw_value):
    try:
        int_value = int(raw_value)
        return(int_value)
    except:
        return("not_integer")

def is_int(value):
    if value == "not_integer":
        return False
    else:
        return True


if __name__ == "__main__":
    main()
