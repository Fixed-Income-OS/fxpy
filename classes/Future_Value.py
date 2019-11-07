from math import pow


class FutureValue:
    def __init__(self, principal, interest_rate, period):
        self.principal = principal
        self.interest_rate = interest_rate
        self.period = period

    def calculate(self):
        return pow(1 + (self.interest_rate / 100), self.period) * self.principal
