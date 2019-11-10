from math import pow
from decimal import Decimal
from utils import period_util


class FutureValue:
    def __init__(self, principal, interest_rate, period, period_type, annuity):
        self.principal = principal
        self.interest_rate = Decimal(interest_rate)
        self.period = period
        self.period_type = period_type
        self.annuity = annuity

    def calculate(self):
        period_cal = period_util.calc_period_info(self.period, self.period_type, self.interest_rate)

        self.period = period_cal['period']
        self.interest_rate = period_cal['interest_rate']

        if self.annuity is False:
            return pow(1 + (self.interest_rate / 100), self.period) * self.principal
        else:
            upper_value = pow(1 + self.interest_rate / 100, self.period) - 1
            return Decimal(self.principal) * (Decimal(upper_value) / Decimal(self.interest_rate / 100))
