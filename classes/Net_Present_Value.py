import numpy as np
from math import pow


class NetPresentValue:
    def __init__(self, cash_flow, discount_rate):
        self.cash_flow = cash_flow
        self.discount_rate = discount_rate
        self.npv = 0

    def calculate(self):
        temp = 0
        to_calc = []

        while temp < len(self.cash_flow):
            cash = self.cash_flow[temp]
            denom = pow((1 + (self.discount_rate / 100)), temp + 1)
            to_calc.append(cash / denom)
            temp += 1

        return np.sum(to_calc)


test = NetPresentValue([2000, 2000, 2500, 4000], 14)
print(test.calculate())
