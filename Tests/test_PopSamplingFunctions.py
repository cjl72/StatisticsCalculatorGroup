import unittest
from PopSamplingFunctions.SimpleSampling import SimpleSampling

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.test = [1,2,3,4,5,6]

    class MyTestCase(unittest.TestCase):
        def setUp(self) -> None:
            seed(3)
            self.testData = randint(0, 50, 15)

    def test_generate_sample(self):
        sample = SimpleSampling.generateSampling(3, self.testData, 5)
        self.assertEqual(sample, [3, 1, 2, 1, 1])





if __name__ == '__main__':
    unittest.main()