from fractions import Fraction
from itertools import *
from random import *
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
# '♡', '♢': red
# '♣', '♠': black
Cards = list(product(Ranks , Suits))

def simualtor_poker2(n):
  count = 0
  for i in range(n):
    index = [randint(0, 51) for i in range(4)]
    list_check=['♡', '♢', '♣', '♠']
    list_result = [Cards[index[i]][1] for i in range(4)]
    # print(list_result)
    if set(list_result) == set(list_check):
      count += 1
  return Fraction(count, n)
print(simualtor_poker2(1000000))
# simualtor_poker2(10)
# print(set(['♡', '♠', '♣', '♠']))
# print(set(['♡', '♠', '♣', '♠']) == set(['♡', '♠', '♣', '♠']))