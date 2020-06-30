import random
class coinFlip(object):
    def flip(numFlips):
        """Assumes numFlips a positive int"""
        heads=0
        for i in range(numFlips):
            if random.choice(('H','T'))=='H':
                heads += 1
        return heads/numFlips
        print(heads/numFlips)

from flippingCoins import coinFlip
from varStdDevCV import variance,stdDev,CV
def flipSim(numFlipsPerTrial,numTrials):
    """Assumes numFlipsPerTrial and numTrials are positive ints"""
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(coinFlip.flip(numFlipsPerTrial))
        #print(fracHeads)#
    mean=sum(fracHeads)/len(fracHeads)
    sd=stdDev(fracHeads)
    return fracHeads,mean,sd
    #print(mean)
