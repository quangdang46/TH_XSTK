E={0,1,2,3,4,5}

from itertools import *
from random import *

def experiment_a():
  list_3_digits =[]
  for i in permutations(E,3):
    digit = int(''.join(map(str,i)))
    digit>99 and list_3_digits.append(digit)
  return list_3_digits

def experiment_b():
  list_4_digits =[]
  for i in permutations(E,4):
    digit = int(''.join(map(str,i)))
    digit>999 and list_4_digits.append(digit)
  return set(list_4_digits)
print(experiment_a())

print(experiment_b())





