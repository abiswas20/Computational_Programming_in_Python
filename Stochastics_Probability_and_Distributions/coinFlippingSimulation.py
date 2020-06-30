import random
from varAndStdDev import variance, stdDev, CV
#from matplotlib import pylab
import matplotlib.pyplot as plt

def makePlot(xVals,yVals,title,xLabel,yLabel,style,logX=False,logY=False):
    plt.figure()
    plt.title(title)
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.plot(xVals,yVals,style)
    if logX:
        plt.semilogx()
    if logY:
        plt.semilogy()
    plt.show()

def runTrial(numFlips):
    """Just one run of the test."""
    numHeads=0
    for n in range(numFlips):
        if random.choice(('H','T'))=='H':
            numHeads+=1
    numTails=numFlips-numHeads
    return (numHeads,numTails)


def flipPlot1(minExp,maxExp,numTrials):
    """Assumes minExp, maxExp and numTrials are ints>0; minExp < maxExp
    Plots summaries of results of numTrials trials of 
    2**minExp to 2**maxExp coin flips."""
    ratiosMeans,diffsMeans,ratiosSDs,diffsSDs,ratioCVs,diffsCVs=[],[],[],[],[],[]
    xAxis=[]
    for Exp in range(minExp,maxExp+1):
        xAxis.append(2**Exp)
    for numFlips in xAxis:
        ratios,diffs=[],[]
        for t in range(numTrials):
            numHeads,numTails=runTrial(numFlips)
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        ratiosMeans.append(sum(ratios)/len(ratios))
        diffsMeans.append(sum(diffs)/len(diffs))
        ratiosSDs.append(stdDev(ratios))
        diffsSDs.append(stdDev(diffs))
        ratioCVs.append(CV(ratios))
        diffsCVs.append(CV(diffs))
    numTrialsString=' ('+str(numTrials)+'Trials)'
    title='Mean Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis,ratiosMeans,title,'Number of flips','Mean Heads/Tails','ko',logX=True,logY=False)
    title='SD Heads/Tails Ratios' + numTrialsString
    makePlot(xAxis,ratiosSDs,title,'Number of flips','Standard deviation','ko',logX=True,logY=True)
    title='Mean abs(#Heads - #Tails)'+numTrialsString
    makePlot(xAxis,diffsMeans,title,'Number of flips','Mean abs(#Heads - #Tails)','ko',logX=True,logY=True)
    title='SD abs(#Heads - #Tails)'+numTrialsString
    makePlot(xAxis,diffsSDs,title,'Number of flips','SD abs(#Heads - #Tails)','ko',logX=True,logY=True)
    title='Coeff. of Var. Heads/Tails Ratio'+numTrialsString
    makePlot(xAxis,ratioCVs,title,'Number of Flips','Coeff. of Var. Heads/Tails Ratio','ko',logX=True)
    title='Coeff. of Var. abs(#Heads - #Tails)'+numTrialsString
    makePlot(xAxis,diffsCVs,title,'Number of Flips','Coeff. of Var. abs(#Heads - #Tails)','ko',logX=True,logY=True)



#test code#
flipPlot1(4,10,1000)  #flipPlot1(minExp,maxExp,numTrials)#
