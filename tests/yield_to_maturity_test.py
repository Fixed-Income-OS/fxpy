import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Yield import Yield


def test_ytm_a():
    test = Yield(11, 1233.64, 19, 6, 1000)
    assert test.yield_to_maturity() == 8.5, "Should be 8.5%"


def test_ytm_b():
    test = Yield(13, 1233.64, 19, 6, 1000)
    assert test.yield_to_maturity() == 10.2, "Should be 10.2%"
