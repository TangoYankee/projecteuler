def welcome():
    """
    welcome message
    """
    print(
        "Welcome! We will find the sum of all the multiples of numbers you select which are below an upper limit you set"
    )


def find_upper_limit():
    """
    the number up to which the multiples will be found and added
    """
    upper_limit_floor = 2
    tries = 0
    while tries < 2:
        upper_limit = input("Please enter your upper limit: ")
        upper_limit = to_int(upper_limit)
        if is_int(upper_limit):
            if upper_limit >= upper_limit_floor:
                return upper_limit
            else:
                print("This integer is not at least 2")
        else:
            print("This is not an integer")
        tries += 1
    return "No correct upper limit entered"


def find_numbers(upper_limit):
    """
    numbers are the base to find all of the multiples
    """
    numbers = []
    enter_more = "y"
    while (enter_more == "y") & (len(numbers) < upper_limit):
        number = input("Please input a number: ")
        number = to_int(number)
        if is_int(number):
            if (number < upper_limit) & (number not in numbers):
                numbers.append(number)
            else:
                print(
                    "This value is not below the upper limit or has already been used"
                )
        else:
            print("This value is not an integer")
        if len(numbers) == 0:
            continue
        else:
            enter_more = input(
                "To input more numbers, enter 'y'. Press any other key to continue: "
            )
    return numbers


def to_int(raw_value):
    """
    convert user input into an integer
    """
    try:
        int_value = int(raw_value)
        return int_value
    except:
        return "not_integer"


def is_int(value):
    """
    validate whether the user input is an integer
    """
    if value == "not_integer":
        return False
    else:
        return True
