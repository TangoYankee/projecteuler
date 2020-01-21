class Set:
    def __init__(self, numbers, upper_limit):
        self.upper_limit = upper_limit
        self.numbers = numbers
        self.master_set = []
        self._find_master_set()

    def get_set(self):
        return self.master_set

    def get_set_sum(self):
        return sum(self.master_set)

    def _find_master_set(self):
        """
        the set of multiples generated from a single number
        """
        for number in self.numbers:
            multiples = Multiples(number, self.upper_limit)
            for multiple in multiples.get():
                if multiple not in self.master_set:
                    self.master_set.append(multiple)


class Multiples:
    def __init__(self, number, upper_limit):
        self.number = number
        self.upper_limit = upper_limit
        self.multiples = []
        self._find_multiples()

    def get(self):
        return self.multiples

    def _find_multiples(self):
        i = 1
        multiple = 0
        while i < self.upper_limit:
            multiple = i * self.number
            if multiple < self.upper_limit:
                self.multiples.append(multiple)
                i += 1
            else:
                break
