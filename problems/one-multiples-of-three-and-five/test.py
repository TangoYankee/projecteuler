import unittest

from multiples import (
    find_master_multiples_set,
    find_all_multiples_sets,
    find_each_multiples_set,
)
from test_data import (
    upper_limit,
    numbers,
    all_multiples_sets_expected,
    master_multiples_sets_expected,
    number,
    each_multiples_set_expected,
)


class TestMasterSet(unittest.TestCase):
    def test_find_master_set(self):
        """
        consolidate sets of multiples into single set with no duplicates
        """
        result = find_master_multiples_set(all_multiples_sets_expected)
        self.assertEqual(result, master_multiples_sets_expected)


class TestAllSets(unittest.TestCase):
    def test_find_all_sets(self):
        """
        find collection of multiples sets for selected numbers
        """
        result = find_all_multiples_sets(numbers, upper_limit)
        self.assertEqual(result, all_multiples_sets_expected)


class TestEachSet(unittest.TestCase):
    def test_find_each_set(self):
        """
        find the set of multiples derived from each number
        """
        result = find_each_multiples_set(number, upper_limit)
        self.assertEqual(result, each_multiples_set_expected)


if __name__ == "__main__":
    unittest.main()
