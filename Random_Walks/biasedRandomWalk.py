###Code below is based on Fig.14.6 in John Guttag's book. coldDrunk and ewDrunk are subclasses of "Drunk" and extends functionality to include random walk scenarios where movement is biased towards a certain direction.###
###simAll is a function that iterates over a sequence of subclasses of Drunk to generate information on how each type behaves.###

import random
from usualAndUnusual import Drunk
class coldDrunk(Drunk):                                             #subclass of Drunk.#
    def takeStep(self):                                             #subclass of Drunk to choose a random step among a list of moves.#
        stepChoices=[(0.0,1.0),(0.0,-2.0),(1.00,0.0),(-1.0,0.0)]    #list of choices of steps.#
        return random.choice(stepChoices)                           #returns randomly chosen step.#

class ewDrunk(Drunk):                                               #ew is a subclass of Drunk.#
    def takeStep(self):                                             #specifies way to handle takeStep for this subclass.#    
        stepChoices=[(1.0,0.0),(-1.0,0.0)]                          #list of choices of steps.#
        return random.choice(stepChoices)                           #returns randomly chosen step.#

from drunkardsWalk import Walk,simWalks,drunkTest
def simAll(drunkKinds,walkLengths,numTrials):
    for dClass in drunkKinds:
        drunkardsWalk.drunkTest(walkLengths,numTrials,dClass)
