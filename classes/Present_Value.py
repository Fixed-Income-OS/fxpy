from math import pow


class PresentValue:
    def __init__(self, fv, r, n):
        self.fv = fv
        self.r = r
        self.n = n

    def denominator(self):
        return pow((1 + self.r / 100), self.n)

    def calculate(self):
        return self.fv / self.denominator()


