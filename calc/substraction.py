""" Subtraction inheriting A and B from Parent calculation class"""
from calc.calculation import Calculation

class Subtraction(Calculation):
    """ Extending the Subtraction class within Calculation"""
    def get_result(self):
        """ Subtraction of A and B"""
        return self.value_a - self.value_b
