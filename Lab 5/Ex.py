import matplotlib.pyplot as plt
from math import *
import numpy as np


# Phân phối Bernoulli
def pmf_bernoulli(p,x):
  return p**x*(1-p)**(1-x)


def plot_pmf_bernoulli(p):
  X=[0,1]
  P_bernoulli=[pmf_bernoulli(p,x) for x in X]
  print(P_bernoulli)
  plt.plot(X,P_bernoulli,'o')

  plt.title('PMF of Bernoulli(p=%.2f)'%(p))
  plt.xlabel('Value')
  plt.ylabel('Probability')
  plt.show()

# plot_pmf_bernoulli(0.5)


# Phân phối nhị thức
def pmf_binom(k,n,p):
  return factorial(n)/(factorial(k)*factorial(n-k))*pmf_bernoulli(p,k)

def plot_pmf_binom(n,p):
  K=list(range(n+1))
  P_binom=[pmf_binom(k,n,p) for k in K]
  plt.plot(K,P_binom,'-o')
  axes=plt.gca()
  axes.set_xlim([0,n])
  axes.set_ylim([0,1.1 *max(P_binom)])
  plt.title('PMF of Bin(%i,%.2f)'%(n,p))
  plt.xlabel('Number k of success')
  plt.ylabel('Probability of k success')
  plt.show()

# plot_pmf_binom(15,0.5)


