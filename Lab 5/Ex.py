import matplotlib.pyplot as plt
from math import *
import numpy as np


# Phân phối Bernoulli
def pmf_bernoulli(p,x):
  return p**x*(1-p)**(1-x)


def plot_pmf_bernoulli(p):
  X=[0,1]
  P_bernoulli=[pmf_bernoulli(p,x) for x in X]
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

# phân phối Poisson


def pmf_poisson(k,lam):
  return lam**k*exp(-lam)/factorial(k)

def plot_pmf_poisson(n,lam):
  K=list(range(n+1))
  P_poisson=[pmf_poisson(k,lam) for k in K]
  plt.plot(K,P_poisson,'-o')
  axes=plt.gca()

  plt.title('PMF of Poisson(%i)'%(lam))
  plt.xlabel('Number k of Events')
  plt.ylabel('Probability of Number of Events')
  plt.show()

# plot_pmf_poisson(25,5)

# Phân bố hình học

def pmf_ge(p,x):
  return p*(1-p)**(x-1)

def plot_pmf_geo(p,n):
  X=list(range(1,n+1))
  P_geo=[pmf_ge(p,x) for x in X]
  plt.plot(X,P_geo,'-o')
  axes=plt.gca()
  axes.set_xlim([1,n])
  axes.set_ylim([0,1.1*max(P_geo)])
  plt.title('PMF of Geometric(%.2f)'%(p))
  plt.xlabel('n')
  plt.ylabel('Probability')
  plt.show()

plot_pmf_geo(0.3,10)
