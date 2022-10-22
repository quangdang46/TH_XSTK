import matplotlib.pyplot as plt
from math import *
import numpy as np

# a 
def pmf_binom(k,n,p):
  return factorial(n)/(factorial(k)*factorial(n-k))*p**k*(1-p)**(n-k)

def pmf_machines(k,n,p):
  return pmf_binom(k,n,p)

print(pmf_machines(2,5,0.1))

# b
def plot_pmf_machines(n,p):
  K=list(range(n+1))
  P_binom=[pmf_machines(k,n,p) for k in K]
  plt.plot(K,P_binom,'-o')
  axes=plt.gca()
  axes.set_xlim([0,n])
  axes.set_ylim([0,1.1 *max(P_binom)])
  plt.title('PMF of Bin(%i,%.2f)'%(n,p))
  plt.xlabel('Number k of success')
  plt.ylabel('Probability of k success')
  plt.show()

plot_pmf_machines(5,0.1)





  




