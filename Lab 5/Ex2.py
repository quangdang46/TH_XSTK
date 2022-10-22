import matplotlib.pyplot as plt
from math import *
import numpy as np

# a
def pmf_poisson(k,lam):
  return lam**k*exp(-lam)/factorial(k)

print(pmf_poisson(2,3))

# b
def plot_pmf_poisson(n,lam):
  K=list(range(n+1))
  P_poisson=[pmf_poisson(k,lam) for k in K]
  plt.plot(K,P_poisson,'-o')
  axes=plt.gca()

  plt.title('PMF of Poisson(%i)'%(lam))
  plt.xlabel('Number k of Events')
  plt.ylabel('Probability of Number of Events')
  plt.show()

plot_pmf_poisson(5,3)



