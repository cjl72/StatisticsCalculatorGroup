import unittest
from MathOperations.Subtraction import Subtraction
from MathOperations.Addition import Addition
from MathOperations.Division import Division

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Addition(self):
        self.assertEqual(3, Addition.sum(1, 2))

    def test_MathOperations_subtraction(self):
        self.assertEqual(1, Subtraction.difference(2, 1))

    def test_MathOperations_divide(self):
        self.assertEqual(2, Division.divide(10, 5))