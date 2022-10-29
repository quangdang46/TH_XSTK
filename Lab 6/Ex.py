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

X=generator_data(4,6,100)
# print(X)