from StatisticFunctions.Mean import Mean
from StatisticFunctions.StandardDeviation import StandardDeviation
from RandomGenerator.PickSeed import PickSeedList
from MathOperations.Division import Division


class Zscore():
    @staticmethod

    def zscore(sd, data):
        X = PickSeedList.pickSeed(sd, data)
        meanData = Mean.mean(data)
        sd = StandardDeviation.standardDeviation(data)
        z = Division.divide(X-meanData, sd)
        return z