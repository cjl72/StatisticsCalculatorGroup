import unittest
from RandomGenerator.RandomNoSeed import RandomNoSeed

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_RandomNoSeed_Int(self):
        result = RandomNoSeed.randomInt(0, 10)
        self.assertEqual(isinstance(result, int), True)

    def test_RandomNoSeed_Dec(self):
        result = RandomNoSeed.randomDec(0, 10)
        self.assertEqual(isinstance(result, float), True)