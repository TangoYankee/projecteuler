import unittest

from multiples_set import Set, Multiples

from test_data import (
    upper_limit,
    numbers,
    master_multiples_set_expected,
    each_multiples_set_expected,
)


class TestMasterSet(unittest.TestCase):
    def test_find_master_set(self):
        """
        consolidate sets of multiples into single set with no duplicates
        """
        master_set = Set(numbers, upper_limit)
        result = master_set.get_set()
        self.assertEqual(result, master_multiples_set_expected)


class TestEachSet(unittest.TestCase):
    def test_find_each_set(self):
        """
        find the set of multiples derived from each number
        """
        each_set = Multiples(numbers[0], upper_limit)
        result = each_set.get()
        self.assertEqual(result, each_multiples_set_expected)


if __name__ == "__main__":
    unittest.main()
