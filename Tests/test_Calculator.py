import unittest

from Calculator.Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calculator_return_sum(self):
        result = self.calculator.add(1, 2)
        self.assertEqual(3, result)

    def test_calculator_return_difference(self):
        result = self.calculator.subtract(2, 1)
        self.assertEqual(1, result)
        
    def test_calculator_return_multiply(self):
        result = self.calculator.multiply(3, 2)
        self.assertEqual(6, result)
    
    def test_calculator_return_divide(self):
        result = self.calculator.divide(10, 5)
        self.assertEqual(2, result)

    def test_calculator_return_exponent(self):
        result = self.calculator.exponent(2, 3)
        self.assertEqual(8, result)

    def test_calculator_return_root(self):
        result = self.calculator.root(4, 2)
        self.assertEqual(2, result)

    def test_calculator_return_log(self):
        result = self.calculator.log(100, 10)
        self.assertEqual(2, result)


