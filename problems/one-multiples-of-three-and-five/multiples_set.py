class Set:
    def __init__(self, numbers, upper_limit):
        """
        a master set of multiples generated from x quantity of numbers, all under a numerical ceiling
        """
        self.upper_limit = upper_limit
        self.numbers = numbers
        self.master_set = []
        self._find_master_set()

    def get_set(self):
        """
        get set of all multiples
        """
        return self.master_set

    def get_set_sum(self):
        """
        get sum of all multiples in set
        """
        return sum(self.master_set)

    def _find_master_set(self):
        """
        single list of all multiples generated from the numbers, no duplicates
        """
        for number in self.numbers:
            multiples = Multiples(number, self.upper_limit)
            for multiple in multiples.get():
                if multiple not in self.master_set:
                    self.master_set.append(multiple)


class Multiples:
    def __init__(self, number, upper_limit):
        """
        the multiples from a number, up to the given numerical ceiling
        """
        self.number = number
        self.upper_limit = upper_limit
        self.multiples = []
        self._find_multiples()

    def get(self):
        """
        get set of multiples from the number
        """
        return self.multiples

    def _find_multiples(self):
        """
        collect the multiples of a number as long as it is below the ceiling
        """
        i = 1
        multiple = 0
        while i < self.upper_limit:
            multiple = i * self.number
            if multiple < self.upper_limit:
                self.multiples.append(multiple)
                i += 1
            else:
                break
