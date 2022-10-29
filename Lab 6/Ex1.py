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



def cdf_normal(x,mu,sigma):
  return (1+erf((x-mu)/(sigma*sqrt(2))))/2

def plot_cdf_normal(mu,sigma):
  X=generator_data(mu-4*sigma,mu+4*sigma,100)
  P_normal=[cdf_normal(x,mu,sigma) for x in X]

  plt.plot(X,P_normal,'r-')
  plt.title('CDF of Normal Distribution(%0.2f,%0.2f)'%(mu,sigma))
  plt.xlabel('X')
  plt.ylabel('P(X)')
  plt.show()

plot_cdf_normal(0,1.5)