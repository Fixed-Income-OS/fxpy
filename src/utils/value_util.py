import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.period_util import calc_period_info
from classes.Future_Value import FutureValue
from decimal import Decimal


def detail_calc_future_value(principal, interest_rate, period, period_type, annuity):
    detail = {'detailed_cash_flow': []}
    period_cal = calc_period_info(period, period_type, interest_rate)

    detail['period_count'] = period_cal['period']
    detail['interest_rate'] = period_cal['interest_rate']
    detail['present_value'] = principal
    detail['annuity'] = annuity

    temp = 1

    while temp <= detail['period_count']:
        future_value = Decimal(FutureValue(principal, interest_rate, temp, period_type, annuity).calculate())

        detail['detailed_cash_flow'].append({'period_count': temp, 'future_value': future_value})
        temp += 1

    return detail
