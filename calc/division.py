""" Division inheriting A and B from Parent calculation class"""
from calc.calculation import Calculation

class Division(Calculation):
    """ Extending the Division class within Calculation"""
    def get_result(self):
        """ Division of A and B"""
        return self.value_a / self.value_b
