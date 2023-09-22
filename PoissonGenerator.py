from __future__ import division
from numpy import *
from pylab import *
from numpy.random import rand
import scipy.stats


#----------------------------www.quant-trading.co-----------------------------------------------------------#

# This algorithm generates Poisson random variables
def Poisson(M,theta):
#M: number of simulations
#theta: average number of jumps

    N = zeros(M)

    for i in range(0,M):
        p = exp(-theta)                     #probability of N = 0 
        F = p                               
        N[i] = 0
        U = rand()
        while U > F:    
            N[i] = N[i]+1
            p = p*theta/N[i]
            F= F+p

    return N


#################################################################################
#scipy function to get the inverse distribution
def Poisson_scipy(M,N,theta):
    N = scipy.stats.distributions.poisson.ppf(rand(M,N),theta)
    return N
