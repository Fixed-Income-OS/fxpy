# Net Present Value

Net present value (NPV) is the difference between the present value of cash inflows 
and the present value of cash outflows over a period of time. 
NPV is used in capital budgeting and investment planning to analyze the profitability 
of a projected investment or project.

More at: [https://www.investopedia.com/terms/n/npv.asp]

```python
from classes.Net_Present_Value import NetPresentValue

discount_rate = 10
cash_flow = [2000, 2000, 2500, 4000]
sample = NetPresentValue(cash_flow, discount_rate)
sample.calculate() # Should be $8,080
```

