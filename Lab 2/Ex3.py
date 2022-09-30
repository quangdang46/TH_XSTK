from fractions import Fraction
from random import *
def simualtor_dice3(n):
  count = 0
  for i in range(n):
    die_1=randint(1,6)
    die_2=randint(1,6)
    if die_1==die_2:
      count+=1
  return Fraction(count, n)

print(simualtor_dice3(1000000))