import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(12, 1) == 13
    assert Calculator.add(0., 5) == 5
    assert Calculator.add(100, 44) == 144
    assert Calculator.add(45, 24) == 69


def test_subtract():
    assert Calculator.subtract(14, 6) == 8
    assert Calculator.subtract(1, 5) == -4
    assert Calculator.subtract(14, -1) == 15
    assert Calculator.subtract(-6, 6) == -12


def test_multiply():
    assert Calculator.multiply(4, 3) == 12
    assert Calculator.multiply(6, 3) == 18
    assert Calculator.multiply(9, 0) == 0
    assert Calculator.multiply(-2, 4) == -8


def test_divide():
    with pytest.raises(ValueError):
        Calculator.divide(73, 0)
    assert Calculator.divide(8, 2) == 4
    assert Calculator.divide(45, 9) == 5
    assert Calculator.divide(18, -6) == -3
    assert Calculator.divide(-8, 8) == -1
