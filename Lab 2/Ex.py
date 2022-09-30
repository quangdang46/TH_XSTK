from fractions import Fraction
from itertools import *
from random import *

def P(event , space):
  return Fraction(len(event & space), len(space))
  
D = {1, 2, 3, 4, 5, 6}
even = {2, 4, 6}
print(P(even, D))


Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))
print(len(Cards))
print(Cards)

def simulator_poker(n):
  count = 0
  for i in range(n):
    index = randint(0, 51)
    if Cards[index][1] == '♡' or Cards[index][1] == '♢':
      count += 1
  return Fraction(count, n)

print(simulator_poker(1000000))


