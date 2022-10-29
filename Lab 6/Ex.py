import matplotlib.pyplot as plt
from math import *


def generator_data(a,b,size):
  n=(b-a)/size
  result = []
  s=a
  while s<b:
    result.append(s)
    s+=n
  if len(result)<size:
    result.append(b)
  return result


# 1 Phân phối đồng nhất

def pmf_uniform_cont(a,b):
  return 1/(b-a)

def plot_pmf_uniform_cont(a,b):
  X=generator_data(a,b,100)
  if b!=a:
    P=[pmf_uniform_cont(a,b) for x in X]

  plt.plot(X,P,'-')
  plt.plot([a,a],[0,1/(b-a)],'g--')
  plt.plot([b,b],[0,1/(b-a)],'g--')

  plt.title('PMF of Uniform Continuous Distribution(%0.2f,%0.2f)'%(a,b))
  plt.show()

# plot_pmf_uniform_cont(4,6)

# 2 Phân phối bình thường
def pmf_normal(x,mu,sigma):
  return exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt(2*pi))

def cdf_normal(x,mu,sigma):
  return (1+erf((x-mu)/(sigma*sqrt(2))))/2

def plot_pmf_normal(mu,sigma):
  X=generator_data(mu-4*sigma,mu+4*sigma,100)
  P_normal=[pmf_normal(x,mu,sigma) for x in X]

  plt.plot(X,P_normal,'-')
  plt.title('PMF of Normal Distribution(%0.2f,%0.2f)'%(mu,sigma))
  plt.xlabel('X')
  plt.ylabel('P(X)')
  plt.show()

plot_pmf_normal(0,1.5)