"""This is the subtraction calculation"""
from calc.calculation import Calculation
class Subtraction(Calculation):
    """result of the the calculation A and B come from calculation parent class"""
    def getresult(self):
        """you need to use self to reference the data contained in the instance of the object."""
        return self.value_a - self.value_b
