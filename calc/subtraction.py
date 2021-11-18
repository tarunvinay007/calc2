"""This is the subtraction calculation"""

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Subtraction(Calculation):
    """The subtraction class"""
    def getresult(self):
        #you need to use self to reference the data contained in the instance of the object.
        return self.value_a - self.value_b
