from itertools import *
from random import *
def P(event, space):
  return len(event)/len(space)

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
# '♡', '♢': red
# '♣', '♠': black

# a
Cards =set(map(lambda x:str(x[0])+x[1], product(Ranks, Suits)))
# print(Cards)

# b

B = list(permutations(Cards, 3))
# print(B)

# c
A1 = set(filter(lambda x: x.count('K') in {1, 2},list(map(lambda x: ''.join(x), list(permutations(Cards, 3))))))
# print(A1)

# d
A2 = set(filter(lambda x: x.count('K')>=1,list(map(lambda x: ''.join(x), list(permutations(Cards, 3))))))
print(round(P(A1, B),4))
print(round(P(A2, B),4))







