import unittest

from StatisticFunctions.Covariance import Covariance
from StatisticFunctions.PopulationCorrelation import PopulationCorrelation
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

    def test_variance_calculator(self):
        v = self.statistics.var(self.testData)
        self.assertEqual(v, 1.25)

    def test_stdDev_calculator(self):
        std = self.statistics.stdDev(self.testData)
        self.assertEqual(std, 1.118033988749895)

    def test_meanDeviation_calculator(self):
        meanDev = self.statistics.meandeviation(self.testData)
        self.assertEqual(meanDev, 1)

    def test_PopulationCorrelation_calculator(self):
        popCo = self.statistics.popCo(PopulationCorrelation.popCor(self.testData, self.testData2))
        self.assertEqual(popCo, -0.22499088742463133)

    def test_RandomNoSeed_Int(self):
        num = self.statistics.randomNoSeedInt(0, 10)
        self.assertEqual(isinstance(num, int), True)

    def test_RandomNoSeed_Dec(self):
        num = self.statistics.randomNoSeedDec(0, 10)
        self.assertEqual(isinstance(num, float), True)

    




