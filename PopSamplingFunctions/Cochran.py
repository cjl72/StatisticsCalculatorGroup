from StatisticFunctions.Zscore import Zscore
from PopSamplingFunctions.MarginError import MarginError
from StatisticFunctions.PopulationProportion import PopulationProportion
from MathOperations.Exponentiation import Exponentiation


class Cochran():
    @staticmethod
    def cochran(sd, data, rnge):


        z = Zscore.zscore(data)
        p = PopulationProportion.proportion(sd, data, rnge)
        e = MarginError.margin(sd, data)
        q = 1 - p

        cochran = (Exponentiation.exponent(z, 2) * p * q)/Exponentiation.exponent(e, 2)

        return cochran