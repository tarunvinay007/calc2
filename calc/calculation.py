"""This is our calculation base class"""
class Calculation:

    #contstructor is instantiated
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        self.value_a = value_a
        self.value_b = value_b
    @classmethod
    def create(cls, value_a, value_b):
        return cls(value_a,value_b)
