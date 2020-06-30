##This is based on Fig.16.6 in John Guttag's book.##

import random
from varStdDevCV import stdDev

#function to calculate area of circle to area of square#
def throwNeedles(numNeedles):
    inCircle=0
    for Needles in range(1,numNeedles+1):
        x=random.random()
        y=random.random()
        if (x**2+y**2)**0.5<=1:
            inCircle+=1
    return 4*(inCircle/numNeedles)


def getEst(numNeedles,numTrials):
    estimates=[]
    for t in range(numTrials):
        piGuess=throwNeedles(numNeedles)
        estimates.append(piGuess)
        sDev=stdDev(estimates)
        curEst=sum(estimates)/len(estimates)
        print('Est. =',str(round(curEst,5))+','+'Needles=',numNeedles)
    return(curEst,sDev)


def estPi(precision,numTrials):
    numNeedles=1000
    sDev=precision
    while sDev>precision/1.96:
        curEst,sDev=getEst(numNeedles,numTrials)
        numNeedles*=2
    return curEst

#Self-Check#
estPi(0.01,100)
