from StatisticFunctions.Mean import Mean

class Variance:
    @staticmethod
    def variance(data):
        m = Mean.mean(data)
        total = 0
        l = len(data)
        for i in data:
            total = total + (i-m)**2
        return (total/l)