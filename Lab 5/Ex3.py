import matplotlib.pyplot as plt
from math import *
import numpy as np

# a
def pmf_ge(p,x):
  return p*(1-p)**(x-1)

print(pmf_ge(0.4,3))

# b
def plot_pmf_ge(n,p):
  X=list(range(1,n+1))
  P_ge=[pmf_ge(p,x) for x in X]
  plt.plot(X,P_ge,'-o')
  axes=plt.gca()
  axes.set_xlim([1,n])
  axes.set_ylim([0,1.1 *max(P_ge)])
  plt.title('PMF of Ge(%.2f)'%(p))
  plt.xlabel('Number x of success')
  plt.ylabel('Probability of x success')
  plt.show()

plot_pmf_ge(10,0.4)



