from fractions import Fraction
from itertools import *
from random import *
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
# '♡', '♢': red
# '♣', '♠': black
Cards = list(product(Ranks , Suits))

def simualtor_poker1(n):
  count = 0
  for i in range(n):
    index = [randint(0, 51) for i in range(5)]
    # print(index)
    if all(Cards[index[i]][1] == '♡' for i in range(5)):
      count += 1
  return Fraction(count, n)
print(simualtor_poker1(1000000))