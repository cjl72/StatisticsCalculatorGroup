from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction

class Calculator:
    Result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def subtract(self, a, b):
        self.Result = Subtraction.difference(a, b)
        return self.Result
