from math import pow


class PresentValue:
    def __init__(self, future_value, interest_rate, period):
        self.future_value = future_value
        self.interest_rate = interest_rate
        self.period = period

    def denominator(self):
        return pow((1 + self.interest_rate / 100), self.period)

    def calculate(self):
        return self.future_value / self.denominator()


