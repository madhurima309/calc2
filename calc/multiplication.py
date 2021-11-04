""" Multiplication inheriting A and B from Parent calculation class"""
from calc.calculation import Calculation

class Multiplication(Calculation):
    """ Extending the Multiplication class within Calculation"""
    def get_result(self):
        """ Multiplication of A and B"""
        return self.value_a * self.value_b
