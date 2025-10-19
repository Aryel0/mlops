import pytest
from src.utils import add, subtract, multiply, divide

def test_add_basic():
    assert add(1, 2, 3) == 6
    assert add(-1, 1) == 0

def test_add_invalid_type():
    with pytest.raises(TypeError):
        add(1, "2", 3)

def test_subtract_basic():
    assert subtract(10, 5) == 5
    assert subtract(10, 3, 2) == 5

def test_subtract_no_args():
    assert subtract() == 0

def test_multiply_basic():
    assert multiply(2, 3, 4) == 24
    assert multiply(5) == 5

def test_multiply_invalid_type():
    with pytest.raises(TypeError):
        multiply("a", 3)

def test_divide_basic():
    assert divide(10, 2) == 5
    assert round(divide(100, 2, 5), 2) == 10.0

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_divide_invalid_type():
    with pytest.raises(TypeError):
        divide(10, "5")
