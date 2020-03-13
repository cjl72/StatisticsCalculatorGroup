import unittest
from RandomGenerator.RandomNoSeed import RandomNoSeed
from RandomGenerator.RandomWithSeed import RandomWithSeed

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_RandomNoSeed_Int(self):
        result = RandomNoSeed.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_RandomNoSeed_Dec(self):
        result = RandomNoSeed.randomDec(0, 10)
        self.assertEqual(isinstance(result, float), True)

    def test_RandomSeed_Int(self):
        result = RandomWithSeed.randomInt(4, 0, 10)
        result2 = RandomWithSeed.randomInt(4, 0, 10)
        self.assertEqual(result, result2)

    def test_RandomSeed_Dec(self):
        result = RandomWithSeed.randomDec(4, 0, 10)
        result2 = RandomWithSeed.randomDec(4, 0, 10)
        self.assertEqual(result, result2)