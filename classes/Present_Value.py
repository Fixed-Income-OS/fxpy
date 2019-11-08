from math import pow
from decimal import Decimal


class PresentValue:
    def __init__(self, future_value, interest_rate, period):
        self.future_value = Decimal(future_value)
        self.interest_rate = Decimal(interest_rate)
        self.period = Decimal(period)

    def discount_rate(self):
        return Decimal(pow(1 / (1 + self.interest_rate / 100), self.period))

    def calculate(self):
        return self.future_value * self.discount_rate()
