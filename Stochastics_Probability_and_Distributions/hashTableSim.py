import random

def simInsertions(numIndices,numInsertions):
    """Assumes numIndices is available number of available has buckets.
    numInsertions to be number of values inserted in them.
    Returns 1 if there is a collision; 0 otherwise."""

    choices=range(numIndices)
    used=[]
    for i in range(numInsertions):
        hashVal=random.choice(choices)
        if hashVal in used:
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices,numInsertions,numTrials):
    collisions=0
    for t in range(numTrials):
        collisions+=simInsertions(numIndices,numInsertions)
    return collisions/numTrials


#Self-Test#
print(findProb(1000,50,10000))
