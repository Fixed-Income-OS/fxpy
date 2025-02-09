def calc_period_info(period, period_type, interest_rate):
    if period_type == 1:
        period = 1 * period
        interest_rate = 1 * interest_rate
    elif period_type == 6:
        interest_rate = interest_rate / 2
        period = 2 * period
    elif period_type == 3:
        interest_rate = interest_rate / 4
        period = 4 * period
    elif period_type == 12:
        interest_rate = interest_rate / 12
        period = 12 * period

    return {'period': period, 'interest_rate': interest_rate}