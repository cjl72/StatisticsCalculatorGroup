import unittest
from StatisticFunctions.Mean import Mean
from StatisticFunctions.Median import Median
from StatisticFunctions.Mode import Mode
from StatisticFunctions.Variance import Variance
from StatisticFunctions.StandardDeviation import StandardDeviation
from StatisticFunctions.MeanDeviation import MeanDeviation

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]
        self.testData2 = [1, 2, 2, 3, 4]

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(2.5, Mean.mean(self.testData))

    def test_StatisticFunctions_Median(self):
        self.assertEqual(2.5, Median.median(self.testData))

    def test_StatisticFunctions_Mode(self):
        self.assertEqual(2, Mode.mode(self.testData2))

    def test_StatisticFunctions_Variance(self):
        self.assertEqual(1.25, Variance.variance(self.testData))

    def test_StatisticFunctions_StandardDeviation(self):
        self.assertEqual(1.118033988749895, StandardDeviation.standardDeviation(self.testData))

    def test_StatisticFunctions_MeanDeviation(self):
        self.assertEqual(1, MeanDeviation.meanDeviation(self.testData))