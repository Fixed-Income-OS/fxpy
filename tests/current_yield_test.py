import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Yield import Yield


def test_current_yield():
    test = Yield(6, 700.89, 18, 6, 1000)
    assert round(test.current_yield(), 2) == 8.56, "Should be 8.56%"
