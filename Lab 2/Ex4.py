from fractions import Fraction
from random import *
def simualtor_dice4(n):
  count = 0
  for i in range(n):
    die_1=randint(1,6)
    die_2=randint(1,6)
    if (die_1==1 and die_2==6) or (die_1==6 and die_2==1):
      count+=1
  return Fraction(count, n)

print(simualtor_dice4(1000000))