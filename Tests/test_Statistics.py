import unittest
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)