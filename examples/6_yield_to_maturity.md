# Yield To Maturity

Yield to Maturity (YTM) is the return from a bond when it matures. Unlike, current yield
yield to maturity takes into account the time value of money i.e., it uses the present value
of all future coupon payments.


```python
from classes.Yield import Yield

coupon_rate = 11
price = 1233.64
period = 19
period_type = 6 
par_value = 1000

sample = Yield(coupon_rate, price, period, period_type, par_value)
sample.calculate() # Should be 8.5%
```

Yield to maturity is computed using the Newton-Raphson method which produces successively better approximations
to the roots of a real-valued function.