class UserInterface:
    upper_limit_floor = 2
    try_limit = 4
    continue_key = "y"

    def __init__(self):
        """
        recieve natural numbers and their upper limit through a command line 
        """
        self._messages()

    def _messages(self):
        """
        guidance for the needs of the system from the user
        """
        self.welcome_message = "Welcome! We will find the sum of all the multiples of numbers you select which are below an upper limit you set"
        self.solution_message = "The sum of the multiples is: "
        self.too_low_alert = "This integer is not at least 2"
        self.not_integer_alert = "This value is not an integer"
        self.try_limit_alert = "No more tries are allowed"
        self.number_request = "Please input a number: "
        self.upper_limit_request = "Please enter your upper limit: "
        self.continue_question = (
            "To input more numbers, enter 'y'. Press any other key to continue: "
        )
        self.too_high_or_repeat_alert = (
            "This value is below zero, above the upper limit, or already used"
        )

    def show_welcome(self):
        """
        welcome message
        """
        print(self.welcome_message)

    def show_solution(self, multiples_sum):
        """
        solution and message explaining
        """
        print(f"{self.solution_message}{multiples_sum}")

    def show_tries_reached(self):
        """
        the user failed to enter a valid value within the given tries
        """
        print(self.try_limit_alert)

    def get_upper_limit(self):
        """
        the natural number up to which the multiples will be found and added.
        limited number of tries
        """
        tries = 0
        while tries < self.try_limit:
            upper_limit_input = UserInput(input(self.upper_limit_request))
            if upper_limit_input.get_is_int():
                upper_limit_int_value = upper_limit_input.get_int_value()
                if upper_limit_int_value >= self.upper_limit_floor:
                    return upper_limit_int_value
                else:
                    print(self.too_low_alert)
            else:
                print(self.not_integer_alert)
            tries += 1
        return False

    def get_numbers(self, upper_limit):
        """
        receive natural numbers from user as long as they want to add more.
        need at least one, with each less than the ceiling, no duplicates,
        and fewer numbers than the value of the ceiling.
        """
        numbers = []
        enter_more = self.continue_key
        while (enter_more == self.continue_key) & ((len(numbers)) < upper_limit):
            number_input = UserInput(input(self.number_request))
            if number_input.get_is_int():
                number_int = number_input.get_int_value()
                if (0 < number_int < upper_limit) & (number_int not in numbers):
                    numbers.append(number_int)
                else:
                    print(self.too_high_or_repeat_alert)
            else:
                print(self.not_integer_alert)
            if len(numbers) == 0:
                continue
            else:
                enter_more = input(self.continue_question)
        return numbers


class UserInput:
    def __init__(self, value):
        """
        state of input from user
        """
        self.value = value
        self._to_int()
        self._is_int()

    def get_int_value(self):
        """
        get the integer version of the value
        """
        return self.int_value

    def get_is_int(self):
        """
        get whether the value is an integer
        """
        return self.is_int

    def _to_int(self):
        """
        convert user input into an integer
        """
        try:
            self.int_value = int(self.value)
        except:
            self.int_value = False

    def _is_int(self):
        """
        validate whether the user input is an integer
        """
        if self.int_value == False:
            self.is_int = False
        else:
            self.is_int = True
