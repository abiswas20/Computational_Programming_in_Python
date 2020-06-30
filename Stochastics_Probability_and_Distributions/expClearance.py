###The code below is based on Fig.15.26 in John Guttag's book. It demonstrates the nature of exponential decay, in specific, and exponential distribution, in general.###
##The probability of unchanged material existing at time t is given by (1-p)**t. p is the probability of an unit of material being altered in an unit of time.## 

import matplotlib.pyplot as plt

def clear(n,p,steps):
    """n: initial number of molecules.
    p: probability of a molecule being cleared.
    steps: number of unit times the process is simulated.
    n and steps are integers."""

    numRemaining=[]
    time=[]
    for s in range(steps):
        time.append(s)
        numRemaining.append(n*(1-p)**s)
    plt.figure(1)
    plt.plot(time,numRemaining)
    plt.title(str(n)+' molecules\n'+str(p)+' probability of molecule being cleared')
    plt.xlabel('time')
    plt.ylabel('molecules remaining')
    plt.show()

    return time,numRemaining

##Self-Test Code##
clear(1000,0.02,1000)
clear(1000,0.01,1000)
clear(1000,0.005,1000)
clear(10000000000,0.005,5000)
