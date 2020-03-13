import unittest
from StatisticFunctions.Mean import Mean

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.testData = [1, 2, 3, 4]

    def test_StatisticFunctions_Mean(self):
        self.assertEqual(2.5, Mean.mean(self.testData))