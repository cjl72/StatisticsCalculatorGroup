import unittest
from Statistics.Statistics import Statistics

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]
        self.testData2 = [1, 2, 2, 3, 4]
        self.statistics = Statistics()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_mean_calculator(self):
        m = self.statistics.mean(self.testData)
        self.assertEqual(m, 2.5)

    def test_median_calculator(self):
        med = self.statistics.median(self.testData)
        self.assertEqual(med, 2.5)

    def test_mode_calculator(self):
        theMode = self.statistics.mode(self.testData2)
        self.assertEqual(theMode, 2)