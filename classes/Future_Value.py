from math import pow
from decimal import Decimal

class FutureValue:
    def __init__(self, principal, interest_rate, period, period_type, annuity):
        self.principal = principal
        self.interest_rate = Decimal(interest_rate)
        self.period = period
        self.period_type = period_type
        self.annuity = annuity

    def calculate(self):
        if self.period_type == 1:
            self.period = 1 * self.period
            self.interest_rate = 1 * self.interest_rate
        elif self.period_type == 6:
            self.interest_rate = self.interest_rate / 2
            self.period = 2 * self.period
        elif self.period_type == 3:
            self.interest_rate = self.interest_rate / 4
            self.period = 4 * self.period
        elif self.period_type == 12:
            self.interest_rate = self.interest_rate / 12
            self.period = 12 * self.period

        if self.annuity is False:
            return pow(1 + (self.interest_rate / 100), self.period) * self.principal
        else:
            upper_value = pow(1 + self.interest_rate / 100, self.period) - 1
            return Decimal(self.principal) * (Decimal(upper_value) / Decimal(self.interest_rate / 100))

    def __str__(self):
        formated = '''
            Principal: ${:,.2f} \n
            Interest rate: {}% per period \n
            Number of payments: {} \n
            Future Value: ${:,.2f}
        '''.format(self.principal, self.interest_rate, self.period, self.calculate())

        return formated
