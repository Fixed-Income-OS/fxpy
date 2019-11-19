# Internal Rate of Return - IRR

THe internal rate of return (IRR) is used to estimate the return on potential investments.
IRR is the rate at which the present value of all cash flows from the investment becomes zero.

![my equation] (https://latex.codecogs.com/gif.download?%5Cdpi%7B120%7D%20%5Clarge%200%20%3D%20NPV%20%3D%20%5Csum%20_%7Bt%3D1%7D%5ET%20%5Cfrac%20%7BC%5Et%7D%7B%281%20+%20IRR%29%5Et%7D%20-%20C_%7B0%7D)

where:

C(t) = Net cash flow during the period t
C(0) = Total initial investment costs
IRR = The internal rate of return
t = The number of time periods

```python
from classes.Internal_Rate_Return import InternalRateReturn

price = 7704
cash_flow = [2000, 2000, 2500, 4000]
sample = InternalRateReturn(-price, cash_flow)
sample.calculate() # Should be 12%
```

