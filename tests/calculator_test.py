"""Testing the Calculator"""
import pprint
import unittest

import pytest

from calculator.calculator import Calculator

#this is how you define a function that will run each time you pass it to a test, it is called a fixture
@pytest.fixture
def clear_history():
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.multiply_numbers(2,5) == 10
    assert Calculator.divide_numbers(10,2) == 5
    assert Calculator.subtract_number(10,10) ==0
    assert Calculator.history_count() == 5

def test_get_last_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.multiply_numbers(-1,5) == -5
    assert Calculator.get_result_of_last_calculation_added_to_history() == -5

def test_get_first_calculation_result(clear_history):
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.multiply_numbers(15, 5) == 75
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(8, 2) == 6

def test_calculator_multiply(clear_history):
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(4,2) == 8

def test_calculator_divide():
    """Testing the divide method of the calculator"""
    assert Calculator.divide_numbers(10,2)== 5

class MyTestCase(unittest.TestCase):
    """A test case is the individual unit of testing.unittest provides a base class"""
    def test_calculator_divide_by_zero(self):
        """Testing the divide method of the calculator when dividing by zero"""
        with self.assertRaises(ZeroDivisionError):
            Calculator.divide_numbers(4,0)
if __name__ == '__main__':
    unittest.main()
