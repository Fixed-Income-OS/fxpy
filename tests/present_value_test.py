import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Present_Value import PresentValue


def test_present_value():
    test = PresentValue(9000000, 7.5, 6)
    assert round(test.calculate()) == 5831654, "Should be $5,831,654"


if __name__ == "__main__":
    test_present_value()


