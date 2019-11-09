import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Future_Value import FutureValue


def test_future_value_regular():
    test_a = FutureValue(10000000, 8.7, 5, 1, False)
    assert round(test_a.calculate()) == 15175665.0, "Should be $15,175,665.0"


def test_future_value_fraction():
    test_b = FutureValue(100000, 5, 7.25, 1, False)
    assert round(test_b.calculate()) == 142437.0, "Should be $142,437.0"


def test_future_value_semi_annual():
    test_c = FutureValue(1000000, 6.4, 6, 6, False)
    assert round(test_c.calculate()) == 1459340.0, "Should be $1,459,340.0"


def test_future_value_annuity():
    test_d = FutureValue(400000, 6.7, 10, 1, True)
    assert round(test_d.calculate()) == 5448885.0,  "Should be $5,448,884"


def test_future_value_annuity_semi_annual():
    test_e = FutureValue(200000, 6.7, 10, 6, True)
    assert round(test_e.calculate()) == 5569558.0, "Should be $5,569,558"


