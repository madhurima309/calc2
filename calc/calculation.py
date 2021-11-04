"""This is going to be the Calculation Object"""

class Calculation:
    # pylint: disable=too-few-public-methods
    """Calculation class """
    def __init__(self,value_a, value_b):
        """initializing value a and b"""
        self.value_a = value_a
        self.value_b = value_b
# Class Factory Method
    @classmethod
    def create(cls, value_a, value_b):
        """creating method """
        return cls(value_a,value_b)
