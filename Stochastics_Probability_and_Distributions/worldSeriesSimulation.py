import matplotlib.pyplot as plt
import random

def simSeries(numSeries):
    prob=0.0
    fracWon,probs=[],[]
    while prob<=1.0:
        fracWon.append(fractionWon(prob,numSeries,7))
        probs.append(prob)
        prob=prob+0.01
    plt.figure(1)
    plt.title(('Probability of Winning '+str(numSeries)+' Series'))
    plt.plot(probs,fracWon,'b',linewidth=4)
    plt.axhline(0.95,color='orange',linewidth=2)
    plt.xlabel('Probability of Team Winning 1 Game')
    plt.ylabel('Probability of Winning Series')
    plt.show()
#    plt.savefig('worldSeries.svg')


def fractionWon(teamProb,numSeries,seriesLen):
    won=0
    for series in range(numSeries):
        if playSeries(seriesLen,teamProb) is True:
            won+=1
    return won/float(numSeries)

def playSeries(numGames,teamProb):
    numWon=0
    for n in range(numGames):
        if random.random()<=teamProb:
            numWon+=1
    return (numWon>(numGames/2))


#Self-Check#
simSeries(4)
simSeries(20)
simSeries(400)
