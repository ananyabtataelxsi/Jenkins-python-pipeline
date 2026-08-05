from app.calculator import add, subtract, multiply, division
import pytest

def test_add():
    assert add(10, 20) == 30

def test_subtract():
    assert subtract(20, 5) == 15

def test_multiply():
    assert multiply(10, 5) == 50

def test_division():
    assert division(20, 5) == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        division(10, 0)