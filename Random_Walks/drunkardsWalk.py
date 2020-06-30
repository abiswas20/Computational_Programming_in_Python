#    """class to simulate drunkard's walk. The 3 methods work as follows:
#    Walk()->Simulates one walk of numSteps steps;
#    simWalk()-> Calls Walk() and simulates numTrials walks of numSteps steps each;
#    drunkTest()-> Calls simWalk() to simulate walks of varying lengths."""

from locationField import Location,Field 
from usualAndUnusual import Drunk, usualDrunk

def Walk(f,d,numSteps):
    """f is the field and d is a drunk. numSteps is the number of steps in a single walk."""
    start=f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps,numTrials,dClass):
    """Assumes numSteps is an int>=0,numTrials an int>0.
    dClass is a subclass of Drunk.Simulates numTrials walks of numSteps each. Returns a list of final distances for each trial"""
    Homer=dClass()
    origin=Location(0,0)
    distances=[]
    for t in range(numTrials):
        f=Field()
        f.addDrunk(Homer,origin)
        distances.append(round(Walk(f,Homer,numSteps),1))
    return distances

def drunkTest(walkLengths,numTrials,dClass):
    for numSteps in walkLengths:
        distances=simWalks(numSteps,numTrials,dClass)
        print(dClass.__name__,'random walk of',numSteps,'steps')
        print('Mean =',round(sum(distances)/len(distances),4))
        print('Max=',max(distances),'Min=',min(distances))




#from locationField import Location,Field
#from usualAndUnusual import usualDrunk
#drunkardsWalk.drunkTest((10,100,1000,10000),100,usualDrunk)
