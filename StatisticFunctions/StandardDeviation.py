from MathOperations.Root import Root
from StatisticFunctions.Variance import Variance

class StandardDeviation:
   @staticmethod
   def standardDeviation(data):
      return Root.root(Variance.variance(data), 2)