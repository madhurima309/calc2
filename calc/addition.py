""" Addition inheriting A and B from Parent calculation class"""
from calc.calculation import Calculation

class Addition(Calculation):
    """ Extending the Addition class within Calculation"""
    def get_result(self):
        """ Addition of A and B"""
        return self.value_a + self.value_b
