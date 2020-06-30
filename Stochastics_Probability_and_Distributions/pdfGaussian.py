##This is based on Fig.15.23. 'gaussian' and 'checkEmpirical' both utilize scipy in their calculations.##
#'gaussian' calculates the probability of 'x' occuring in a gaussian distribution.#
#'checkEmpirical' evaluates the fraction that falls within certain standard deviation of mean.#

import scipy.integrate
import matplotlib.pyplot as plt

def gaussian(x,mu,sigma):
    factor1=(1.0/(sigma*((2*scipy.pi)**0.5)))
    factor2=scipy.e**(-(((x-mu)**2)/(2*sigma**2)))
    return factor1*factor2

from pdfGaussian import gaussian
import random

def checkEmpirical(numTrials):
    for t in range(numTrials):
        mu=random.randint(-10,10)
        sigma=random.randint(1,10)
        print('For mu = ', mu, 'and sigma = ',sigma)
        for numStd in (1,2,3,4,5):
            area=scipy.integrate.quad(gaussian, mu-numStd*sigma,
                    mu+numStd*sigma,(mu,sigma))[0]
            print(' Fraction within',numStd,'std = ', round(area,4))

#Self-Check#
checkEmpirical(5)
