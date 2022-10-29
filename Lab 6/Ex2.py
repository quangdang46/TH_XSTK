import matplotlib.pyplot as plt
from math import *



def pmf_normal(x,mu,sigma):
  return exp(-(x-mu)**2/(2*sigma**2))/(sigma*sqrt(2*pi))

def cdf_normal(x,mu,sigma):
  return (1+erf((x-mu)/(sigma*sqrt(2))))/2


def solve(mu, sigma, a, b):
  return cdf_normal(b, mu, sigma) - cdf_normal(a, mu, sigma)

print(solve(10, 1, 9, 12))
