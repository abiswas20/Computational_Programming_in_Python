from locationField import Location, Field
from drunkardsWalk import Walk,simWalks,drunkTest
from iteratingStyles import styleIterator
from usualAndUnusual import Drunk, usualDrunk
from biasedRandomWalk import coldDrunk, ewDrunk

class plotRandomWalks():

    """The code below is based on Fig.14.8. It plots drunkard's walk for different types of drunk. This can be considered as an extension to "test_simAll.py" for graphical representation. Plot styles are iterated between 'm-','r:','k-.' by the class styleIterator"""

    def simDrunk(numTrials,dClass,walkLengths):
        """This method does not affect the result of the simulation. Simulations like this can take a long time and printing an occasional messages is reassuring to the client of the class."""
        meanDistances=[]
        for numSteps in walkLengths:
            print('Starting simulation of', numSteps,'steps')
            trials=simWalks(numSteps,numTrials,dClass)
            mean=sum(trials)/len(trials)
            meanDistances.append(mean)
        return meanDistances


from matplotlib import pylab 
from plottingWalks import plotRandomWalks

def simAll1(drunkKinds,walkLengths,numTrials):
    """This method plots random walks of each type of drunk. Each case is drawn in a different style, chosen by styleIterator."""
    styleChoice=styleIterator(('m-','r:','k-.'))
    for dClass in drunkKinds:
        curStyle=styleChoice.nextStyle()
        print('Starting simulation of',dClass.__name__)
        means = plotRandomWalks.simDrunk(numTrials,dClass,walkLengths)
        print(means)
        pylab.plot(walkLengths,means,curStyle,label=dClass.__name__)
    pylab.title('Mean distance from Origin ('+str(numTrials)+'trials)'
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc='best')
    pylab.semilogx()
    pylab.semilogy()




