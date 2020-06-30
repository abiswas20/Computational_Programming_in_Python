###The code below is based on Fig.15.3."flippingCoins.py" contains code that can simulate numTrials number of sets of numFlips number of flips each.###
###The objective of this specific exercise is to see if a trial subsequent to a particularly extreme trial is closer to expected value.###

import random
from flippingCoins import coinFlip
import matplotlib.pyplot as plt

def regressionToMean(numFlips,numTrials):
    fracHeads=[]
    for t in range(numTrials):
        fracHeads.append(coinFlip.flip(numFlips))
    #next section keeps count of trials with extreme results and the subsequent trial.#
    extremes,nextTrials=[],[]
    for i in range(len(fracHeads)-1):
        if fracHeads[i]>0.66 or fracHeads[i]<0.33:
            extremes.append(fracHeads[i])
            nextTrials.append(fracHeads[i+1])
            print(i*100/len(fracHeads),"percent complete")
        i+=1
    print(extremes,nextTrials)
    if len(extremes)!=0:
        avg_extremes=sum(extremes)/len(extremes)
        print(avg_extremes)
    if len(nextTrials)!=0:
        avg_nextTrials=sum(nextTrials)/len(nextTrials)        
        print(avg_nextTrials)
    #plotting results#
    plt.figure(1)
    plt.title('Regression to the Mean')
    plt.plot(range(len(extremes)),extremes,'ko',label='Extreme')
    plt.plot(range(len(nextTrials)),nextTrials,'k^',label='nextTrial')
    plt.axhline(0.5)
    plt.ylim(0,1)
    plt.xlim(-1,len(extremes)+1)
    plt.xlabel('Extremes and Next Trial')
    plt.ylabel('Fraction Heads')
    plt.legend(loc='best')
    plt.show()
    
    return [avg_extremes, avg_nextTrials]


print(regressionToMean(100,100000))
