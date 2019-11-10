class Yield:
    def __init__(self, coupon_rate, price, par_value=1000):
        self.coupon_rate = coupon_rate
        self.price = price
        self.par_value = par_value

    def current_yield(self):
        annual_coupon_interest = self.par_value * (self.coupon_rate / 100)

        return (annual_coupon_interest / self.price) * 100


