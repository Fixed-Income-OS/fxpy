import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from classes.Internal_Rate_Return import InternalRateReturn


def test_irr_one():
    test = InternalRateReturn(-7704, [2000, 2000, 2500, 4000])
    assert round(test.calculate()) == 12, "Should be 12%"


def test_irr_two():
    test = InternalRateReturn(-7348, [2000, 2000, 2500, 4000])
    assert round(test.calculate()) == 14, "Should be 14%"


def test_irr_three():
    test = InternalRateReturn(-8080, [2000, 2000, 2500, 4000])
    assert round(test.calculate()) == 10, "Should be 10%"
