import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.period_util import calc_period_info


def cash_flow(coupon_rate, period, period_type=6, par_value=1000):
    result = []
    future_value = par_value

    period_cal = calc_period_info(period, period_type, coupon_rate)

    period_count = period_cal['period']
    payment = (period_cal['interest_rate'] * future_value) / 100

    temp = 1

    while temp <= period_count - 1:
        result.append(payment)
        temp += 1

    result.append(par_value + payment)
    return result
