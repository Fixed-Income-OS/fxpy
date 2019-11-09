import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from classes.Price_Bond_Regular import PriceBondRegular


def test_px_bond_reg_one():
    test = PriceBondRegular(9, 20, 6, 12, 1000)
    assert round(test.calculate()) == 774, "Should be $774"
