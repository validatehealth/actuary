import unittest  # similar to testthat library in R
from RateTable import RateTable


class RateTableTest(unittest.TestCase):

    def setUp(self):  # anything done in setup is available for each test.  Tests are isolated from one another.
        self.rate_table = RateTable(65, 75, 5, True)
        self.rate_table.set_rates([1000, 1500, 2000])

    def test_ages(self):  # needs to start with test_
        ages = self.rate_table.ages
        self.assertEqual(ages, list(range(65, 76, 5)))

    def test_setting_rates(self):
        rate_table = self.rate_table
        self.assertEqual(rate_table.get_rate(72), 1500)


if __name__ == '__main__':
    unittest.main()