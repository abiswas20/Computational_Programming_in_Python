import random
from usualAndUnusual import Drunk, usualDrunk
from locationField import Field 
from locationField import Location
from drunkardsWalk import Walk,simWalks,drunkTest
from biasedRandomWalk import coldDrunk, ewDrunk

def simAll(drunkKinds,walkLengths,numTrials):
    for dClass in drunkKinds:
        drunkTest(walkLengths,numTrials,dClass)

simAll((usualDrunk,coldDrunk,ewDrunk),(100,1000),1000)
