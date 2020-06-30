###The code below is based on Fig.15.19 in John Guttag's book.###

import random
from varStdDevCV import variance,stdDev,CV
import matplotlib.pyplot as plt

def flip(numFlips):
    """Assumes numFlips to be a positive int."""
    heads=0
    for i in range(numFlips):
        if random.choice(('H','T'))=='H':
            heads+=1
    return heads/float(numFlips)

def flipSim(numFlipsPerTrial,numTrials):
    """Assumes numFlipsPerTrial and numTrials are positive int."""
    fracHeads=[]
    for i in range(numTrials):
        fracHeads.append(flip(numFlipsPerTrial))
    mean=sum(fracHeads)/len(fracHeads)
    var=variance(fracHeads)
    sd=stdDev(fracHeads)
    cv=CV(fracHeads)
    return (fracHeads,mean,sd)

def labelPlot(numFlips,numTrials,mean,sd):
    """Label and annotate plots. Annotations to add statistics from data included in the plot."""
    plt.title(str(numTrials)+' trials of '+str(numFlips)+ 'flips each')
    plt.xlabel('Fraction of Heads')
    plt.ylabel('Number of Trials')
    plt.annotate('Mean = '+ str(round(mean,4))\
            +'\nSD = '+ str(round(sd,4)), size='x-large', 
            xycoords='axes fraction', xy=(0.67,0.5))

def makePlots(numFlips1,numFlips2,numTrials):
    """Specifics of plots to be drawn"""
    val1,mean1,sd1=flipSim(numFlips1,numTrials)
    plt.hist(val1,bins=20)
    xmin,xmax=plt.xlim()
    labelPlot(numFlips1,numTrials,mean1,sd1)
    plt.figure()
    plt.show()
    val2,mean2,sd2=flipSim(numFlips2,numTrials)
    plt.hist(val2,bins=20)
    plt.xlim(xmin,xmax)
    labelPlot(numFlips2,numTrials,mean2,sd2)
    plt.figure()
    plt.show()


makePlots(100,1000,100000)

