# Future Value

A generalized future value formula is as follows:

FV = P (1 + i)^N

- FV = Future Value ($);
- P = Original principal ($);
- i = Interest rate (in decimal form);
- N = Number of years;

```python
from classes.Future_Value import FutureValue

principal = 10000000
interest_rate = 8.7
period = 5
period_type = 1 # Annual
annuity = False

sample = FutureValue(principal, interest_rate, period, period_type, annuity)
sample.calculate() # $15,175,665.0
```