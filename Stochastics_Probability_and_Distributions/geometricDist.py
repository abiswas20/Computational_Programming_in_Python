###Code below is based on Fig.29 in John Guttag's book. Given that  successProb is the probability of a single attempt being successful, the code simulates the number of attempts needed before a success.###

import random
import matplotlib.pyplot as plt

def successfulStarts(successProb,numTrials):
    triesBeforeSuccess=[]
    for t in range(numTrials):
        consecFailures=0
        while random.random()>successProb:
            consecFailures+=1
        triesBeforeSuccess.append(consecFailures)
    return triesBeforeSuccess

probOfSuccess=(1/250)
numTrials=10000000
distribution=successfulStarts(probOfSuccess,numTrials)
plt.hist(distribution,bins=10)
plt.xlabel('Tries before Success')
plt.ylabel('Number of Occurences out of 1 Million')
plt.title('Probability of a Try being Successful: '\
        +str(round(1/250,3)))
plt.show()
