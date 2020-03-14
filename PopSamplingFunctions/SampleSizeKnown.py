from PopSamplingFunctions.MarginError import MarginError
from StatisticFunctions.StandardDeviation import StandardDeviation
from MathOperations.Exponentiation import Exponentiation

class SampleSizeKnownPop():
    @staticmethod

    def sampleSize(sd, data):

        e = MarginError.marginError(sd, data)
        stdDev = StandardDeviation.standardDeviation(data)
        val = (1.96 * stdDev) / e
        sample = Exponentiation.exponent(val, 2)

        return sample