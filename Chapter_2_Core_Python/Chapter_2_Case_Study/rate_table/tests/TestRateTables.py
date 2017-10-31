import unittest  # similar to testthat library in R
from ..RateTable import RateTable


class RateTableTest(unittest.TestCase):

    def setUp(self):  # anything done in setup is available for each test.  Tests are isolated from one another.
        self.rate_table = RateTable(65, 115, 5, True)

    def test_ages(self):  # needs to start with test_
        ages = self.rate_table.ages
        self.assertEqual(ages, list(range(65, 115, 5)))

    def test_setting_rates(self):
        pass


if __name__ == '__main__':
    unittest.main()