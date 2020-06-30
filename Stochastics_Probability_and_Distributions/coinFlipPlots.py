#The following code is based on Fig.15.5 in John Guttag's book on computational science.It shows how the law of large numbers impact raw difference in the number of heads and tails and the ratio of heads/tails.#

import random
import matplotlib.pyplot as plt
def flipPlot(minExp,maxExp):
    """Assumes minExp and manExp are positive integers. 
    Plots the results of 2**minExp to 2**maxExp coin flips.
    The values plotted are i)ABS(#Heads-#Tails) and ii)#Heads/#Tails."""
    ratios,diffs,xAxis=[],[],[]
    for exp in range(minExp,maxExp+1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads=0    
        for n in range(numFlips):
            if random.choice(('H','T'))=='H':
                numHeads+=1
        numTails=numFlips-numHeads
        try:
            ratios.append(numHeads/numTails)
            diffs.append(abs(numHeads-numTails))
        except ZeroDivisionError:
            continue
    #plotting part#
    plt.figure('Fig.1')
    plt.title('Abs(#Heads-#Tails) vs Number of Flips')
    plt.xlabel('Number of Flips')
    plt.ylabel('Abs(#Heads-#Tails)')
    plt.plot(xAxis,diffs,'k')
    plt.show()
    plt.figure('Fig.2')
    plt.title('#Heads/#Tails vs Number of Flips')
    plt.xlabel('Number of Flips')
    plt.ylabel('#Heads/#Tails')
    plt.plot(xAxis,ratios,'k')
    plt.show()
    plt.figure('Fig.3')
    plt.title('#Heads/#Tails vs Abs(#Heads-#Tails)')
    plt.xlabel('Abs(#Heads-#Tails)')
    plt.ylabel('#Heads/#Tails')
    plt.plot(diffs,ratios,'k')
    plt.show()

#test code#
#random.seed(0)
flipPlot(4,20)
