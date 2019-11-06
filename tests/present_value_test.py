import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Present_Value import PresentValue


def test_present_value():
    test = PresentValue(200, 3, 10)
    assert test.calculate() == 148.818782979345, "Should be 148.818782979345"


if __name__ == "__main__":
    test_present_value()


