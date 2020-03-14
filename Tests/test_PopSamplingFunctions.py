import unittest
from random import randint, seed

from PopSamplingFunctions.SimpleSampling import SimpleSampling
from PopSamplingFunctions.SystematicSampling import SystematicSampling
from PopSamplingFunctions.ConfidenceInterval import ConfidenceInterval


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1,2,3,4,5,6]

    class MyTestCase(unittest.TestCase):
        def setUp(self) -> None:
            seed(3)
            self.testData = randint(0, 20)

    def test_generate_sample(self):
        result = SimpleSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(result, [3, 1, 2, 1, 1])

    def test_SystematicSampling(self):
        result = SystematicSampling.systematicSampling(self.testData)
        self.assertEqual(result, [3, 21, 43, 21, 20])

    def test_ConfidenceInterval(self):
        result = ConfidenceInterval.confidenceInterval(.90, 1, 5, self.testData)
        self.assertEqual(result, (0.8046719486285641, 3.9953280513714358))





if __name__ == '__main__':
    unittest.main()