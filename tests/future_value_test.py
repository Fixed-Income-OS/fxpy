import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Future_Value import FutureValue


def test_future_value():
    test = FutureValue(10000000, 8.7, 5)
    assert test.calculate() == 15175664.630142067, "Should be 15175664.630142067"


if __name__ == "__main__":
    test_future_value()


