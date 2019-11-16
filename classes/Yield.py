import scipy.optimize as optimize


class Yield:
    def __init__(self, coupon_rate, price, period, period_type, par_value=1000):
        self.coupon_rate = coupon_rate
        self.price = price
        self.period = period
        self.period_type = period_type
        self.par_value = par_value

    def current_yield(self):
        annual_coupon_interest = self.par_value * (self.coupon_rate / 100)

        return (annual_coupon_interest / self.price) * 100

    def yield_to_maturity(self):
        guess = 0.05
        freq = float(self.period)
        periods = self.period * freq
        coupon = self.coupon_rate / 100. * self.par_value / freq
        dt = [(i + 1) / freq for i in range(int(periods))]

        def ytm_func(y):
            for t in dt:
                initial_sum = []
                for t in dt:
                    initial_sum.append(coupon / (1 + y / freq) ** (freq * t))

                return sum(initial_sum) + self.par_value / (1 + y / freq) ** (freq * t) - self.price

        return round(optimize.newton(ytm_func, guess) * 100, 1)



