##The function below draws error bar showing 95% confidence interval. 95% CI coincides with 1.96x standard deviation. As the number of flips increases per trial, the confidence interval becomess tighter.##

from flippingCoins import coinFlip,flipSim
import matplotlib.pyplot as plt
from varStdDevCV import variance,stdDev,CV
import numpy as np

def showErrorBars(minExp,maxExp,numTrials):
    """Assumes minExp and maxExp are positive integers and maxExp>minExp.
    numTrials is also a positive integer.
    Plots mean fraction of heads with error bars."""

    means,sds,xVals=[],[],[]
    i=0
    for exp in range(minExp,maxExp+1):
        xVals.append(2**exp)
        fracHeads,mean,sd=flipSim(2**exp,numTrials)
        means.append(mean)
        sds.append(sd)
        plt.errorbar(xVals,means,yerr=1.96*np.array(sds))
        plt.semilogx()
        plt.title('Mean Fraction of Heads (' + str(numTrials) + ' Trials)')
        plt.xlabel('Number of flips per trial')
        plt.ylabel('Fraction of heads with 95% CI')
        print(str(round((i+1)*100/np.count_nonzero(range(minExp,maxExp+1)),2)) + ' pct. progress...')
        i=i+1
    plt.show()
    
    return str(np.array(sds)), str(sds)


#Self-Check#
showErrorBars(3,26,100)
