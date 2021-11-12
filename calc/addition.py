"""This is the addition calculation"""
from calc.calculation import Calculation
class Addition(Calculation):
    """method to get result of calculation A and B come from calculation parent class"""
    def getresult(self):
        """self to reference the data contained in the instance of the object."""
        return self.value_a + self.value_b
