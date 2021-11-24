"""This is the addition calculation"""

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """The addition class"""
    def getresult(self):
        """class"""
        return self.value_a + self.value_b
