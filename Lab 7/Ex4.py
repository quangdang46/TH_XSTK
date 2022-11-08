from itertools import *
from random import *


def cross(a, b):
  return [s+t for s in a for t in b]

urn=cross('W','12')+ cross('B','123') + cross('R','1234')

U3 = list(combinations(urn, 3))

white1blue1red1 = list(filter(lambda x: {'R','B','W'}.issubset(set(map(lambda x:x[0],x))), U3))
print(white1blue1red1)

P = len(white1blue1red1)/len(U3)
print(P)