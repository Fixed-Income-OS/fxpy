# Present Value

A generalized present value formula is as follows:

PV = FV [1 / (1 + i)^N]

- FV = Future Value ($);
- P = Original principal ($);
- i = Interest rate (in decimal form);
- N = Number of years;

```python
from classes.Present_Value import PresentValue

principal = 9000000
interest_rate = 7.5
period = 6
period_type = 1 # Annual
annuity = False

sample = PresentValue(principal, interest_rate, period, period_type, annuity)
sample.calculate() # $5,831,654
```