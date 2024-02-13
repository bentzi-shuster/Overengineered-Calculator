import pytest
from decimal import Decimal

from calculator import Calculator

# Define test data for various operations
testdata_add = [
    ([1, 2, 3, 4, 5], 15),
    ([0, 0, 0], 0),
    ([-1, 1], 0),
]

testdata_subtract = [
    ((10, 2, 3), 5),
    ((0, 0, 0), 0),
    ((5, 2, 1), 2),
]

testdata_multiply = [
    ((1, 2, 3, 4), 24),
    ((-1, 2, -3), 6),
]

testdata_divide = [
    ((10, 2), 5),
    ((0, 5), 0),
    ((3, 3), 1),
]

testdata_factorial = [
    (5, 120),
    (0, 1),
]

# Use pytest.mark.parametrize to create parameterized tests
@pytest.mark.parametrize("input_args, expected_result", testdata_add)
def test_addition(input_args, expected_result):
    result = Calculator.add(*input_args)
    assert result == Decimal(expected_result)

@pytest.mark.parametrize("input_args, expected_result", testdata_subtract)
def test_subtraction(input_args, expected_result):
    result = Calculator.subtract(*input_args)
    assert result == Decimal(expected_result)

@pytest.mark.parametrize("input_args, expected_result", testdata_multiply)
def test_multiplication(input_args, expected_result):
    result = Calculator.multiply(*input_args)
    assert result == Decimal(expected_result)

@pytest.mark.parametrize("input_args, expected_result", testdata_divide)
def test_division(input_args, expected_result):
    result = Calculator.divide(*input_args)
    assert result == Decimal(expected_result)

@pytest.mark.parametrize("input_arg, expected_result", testdata_factorial)
def test_factorial(input_arg, expected_result):
    result = Calculator.factorial(input_arg)
    assert result == Decimal(expected_result)
