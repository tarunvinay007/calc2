"""This is the subtraction calculation"""
from calc.calculation import Calculation
class Subtraction(Calculation):
    """The subtraction class"""
    def getresult(self):
        """self"""
        return self.value_a - self.value_b
