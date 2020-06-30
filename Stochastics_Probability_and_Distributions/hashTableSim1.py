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
    avgCollisions=[]
    for n in numInsertions:
        collisions=[]
        k=numTrials
        while k>=0:
            collisions.append(simInsertions(numIndices,n))
            k-=1
        avgCollisions.append(sum(collisions)/len(collisions))
            
    return avgCollisions


#Self-Test#
print(findProb(1000,[25,50,100],10000))
