"""
This class is used to represent an actuarial rate table
"""


class RateTable:

    def __init__(self, age_start, age_end, step, left):
        """
        This initializes the rates based on a start and end age
        Parameters
        __________
        age_start: the starting age
        age_end: the ending age
        step: the width of each age band
        left: whether or not an age will match the left endpoint or right endpoint
        """
        self.age_start = age_start
        self.age_end = age_end
        self.step = step
        self.ages = list(range(age_start, age_end + 1, step)) # Need to add one to include age_end
        self.left = left
        self.rates = []

    def set_rates(self, rates):
        """
        Set the rates for every age band
        :param rates: a list of rates for the age band
        :return: whether or not the rates were set for the rate table
        """
        if len(rates) == len(self.ages):
            self.rates.extend(rates)
            return True
        else:
            return False

    def get_rate(self, age):
        """
        Get a single rate for a given age
        :param age: the lookup age
        :return: the rate for the lookup age or 0 if the rates are not set for the rate table
        """
        ages = self.ages
        left = self.left
        rates = self.rates
        if len(rates) == 0:
            return 0
        if age <= min(ages):
            age_index = ages.index(min(ages))
        elif age >= max(ages):
            age_index = ages.index(max(ages))
        else:
            greater_than_age = list(map(lambda x: age < x, ages))
            age_index = greater_than_age.index(True)
            if left:
                age_index = age_index - 1
        return rates[age_index]

    def __repr__(self):
        ages = self.ages
        rates = self.rates
        if len(rates) > 0:
            table_rows = ['Age {} has rate {}'.format(age, rate) for age, rate in zip(ages, rates)]
        else:
            table_rows = ['Age {}'.format(age) for age in ages]
        return '\n'.join(table_rows)
