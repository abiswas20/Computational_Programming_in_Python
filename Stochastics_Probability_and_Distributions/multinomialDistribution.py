###The following code is in response to a finger exercise in John Guttag's book (on the page just before Fig.15.26).###
##Problem Statement: Implement a function that calculates: a) the probability of rolling exactly two 3's in k rolls of a fair die.##
##Also use this function to: b) plot the probability as k varies from 2 to 100.##

import math

def diceProbability(K,k1,p):    #K-->number of independent trials; k1-->number of successes; p-->probability of success in a single trial.#
    probability,timesPerTrial,numSuccess=[],[],[]
    for s in range(2,k1,1):
        numSuccess.append(s)
        for k in range(2,K,1):
            timesPerTrial.append(k)
            probability.append(math.factorial(k)/((math.factorial(s))*(math.factorial(k-s)))*(p**k)*((1-p)**(k-s)))
            print(numSuccess,timesPerTrial,probability)
### Need to verify. Signed 2/7/20. ###            


diceProbability(20,10,(1/6))
