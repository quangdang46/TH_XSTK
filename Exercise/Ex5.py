from itertools import *
from random import *
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))


# def getSuits(arr):
#   return [x[1] for x in arr]
# def getRanks(arr):
#   return [x[0] for x in arr]

# def experiment_a(n):
#   count=0
#   for _ in range(n):
#     listRandom=getRanks(choices(Cards,k=5))
#     if len(set(listRandom))==5 and max(listRandom)-min(listRandom)==4:
#       count+=1
#   return count/n

# print(experiment_a(1000000))