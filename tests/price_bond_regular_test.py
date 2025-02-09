import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from classes.Price_Bond_Regular import PriceBondRegular


def test_px_bond_reg_one():
    test = PriceBondRegular(9, 20, 6, 12, 1000)
    assert round(test.calculate()) == 774, "Should be $774"


def test_px_bond_price():
    sample = PriceBondRegular(5.75, 1.5, 6, 0.093691, 100)
    assert round(sample.price_bond()) == 95, "Should be $95"


def test_px_bond_price():
    sample = PriceBondRegular(5.75, 1.5, 12, 0.093691, 100)
    assert round(sample.price_bond()) == 22, "Should be 22"
