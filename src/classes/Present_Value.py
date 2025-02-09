from math import pow
from decimal import Decimal
from utils import period_util


class PresentValue:
    def __init__(self, par_value, interest_rate, period, period_type, annuity):
        self.par_value = Decimal(par_value)
        self.interest_rate = Decimal(interest_rate)
        self.period = Decimal(period)
        self.period_type = Decimal(period_type)
        self.annuity = annuity

    def discount_rate(self):
        return Decimal(pow(1 / (1 + self.interest_rate / 100), self.period))

    def calculate(self):
        period_cal = period_util.calc_period_info(self.period, self.period_type, self.interest_rate)

        self.period = period_cal['period']
        self.interest_rate = period_cal['interest_rate']

        if self.annuity is False:
            return self.par_value * self.discount_rate()
        else:
            return self.par_value * Decimal((1 - self.discount_rate()) / (self.interest_rate / 100))
