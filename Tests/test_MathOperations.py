import unittest
from MathOperations.Subtraction import Subtraction
from MathOperations.Addition import Addition
from MathOperations.Division import Division
from MathOperations.Multiplication import Multiplication
from MathOperations.Exponentiation import Exponentiation
from MathOperations.Root import Root

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(1, Subtraction.difference(2, 1))

   def test_MathOperations_return_Multiplication(self):
        self.assertEqual(6, Multiplication.multiply(3, 2))
        
    def test_MathOperations_divide(self):
        self.assertEqual(2, Division.divide(10, 5))

    def test_MathOperations_exponentation(self):
        self.assertEqual(8, Exponentiation.exponent(2, 3))

    def test_MathOperations_root(self):
        self.assertEqual(2, Root.root(4, 2))



