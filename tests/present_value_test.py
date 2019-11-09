import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Present_Value import PresentValue


def test_present_value():
    test = PresentValue(9000000, 7.5, 6, 1, False)
    assert round(test.calculate()) == 5831654, "Should be $5,831,654"


def test_present_value_fraction():
    test = PresentValue(1000, 7, 9.25, 1, False)
    assert round(test.calculate()) == 535, "Should be $534.81"


def test_present_value_annuity():
    test = PresentValue(100, 6.25, 5, 1, True)
    assert round(test.calculate()) == 418, "Should be $418"


def test_present_value_annuity_multiple():
    test = PresentValue(50, 6.25, 5, 6, True)
    assert round(test.calculate()) == 424, "Should be $424"


if __name__ == "__main__":
    test_present_value()
    test_present_value_fraction()
    test_present_value_annuity()
    test_present_value_annuity_multiple()
