from scipy.stats import sem, t

from PopSamplingFunctions.ConfidenceIntervalPop import ConfidenceIntervalPop
from PopSamplingFunctions.SimpleSampling import SimpleSampling


class ConfidenceInterval(ConfidenceIntervalPop):
    @staticmethod
    def confidenceInterval(conf, data, sd, higher):
        sample = SimpleSampling.generateSampling(sd, data, higher)
        return ConfidenceIntervalPop.confidenceIntervalPop(conf, sample)