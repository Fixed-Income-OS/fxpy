import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Net_Present_Value import NetPresentValue


def test_npv_one():
    test = NetPresentValue([2000, 2000, 2500, 4000], 10)
    assert round(test.calculate()) == 8081, "Should be $8,080"


def test_npv_two():
    test = NetPresentValue([2000, 2000, 2500, 4000], 12)
    assert round(test.calculate()) == 7702, "Should be $7,702"

