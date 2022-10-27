from itertools import *
from random import *
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))



def getSuits(arr):
  return [x[1] for x in arr]
def getRanks(arr):
  return [x[0] for x in arr]


def experiment_a(n):
  count=0
  for _ in range(n):
    listRandom=getSuits(choices(Cards,k=4))
    if len(set(listRandom))==1:
      count+=1
  return count/n

def experiment_b(n):
  count=0
  for _ in range(n):
    listRandom=getSuits(choices(Cards,k=4))
    if len(set(listRandom))==4:
      count+=1
  return count/n

def experiment_c(n):
  count=0
  for _ in range(n):
    listRandom=set(getSuits(choices(Cards,k=4)))
    if (len(listRandom)==2 and (listRandom.issubset({'♡','♢'}) or listRandom.issubset({'♣','♠'}))) or len(listRandom)==1:
      count+=1
  return count/n

def experiment_d(n):
  count=0
  for _ in range(n):
    listRandom=getRanks(choices(Cards,k=4))
    if len(set(listRandom))==1:
      count+=1
  return count/n

def experiment_e(n):
  count=0
  for _ in range(n):
    listRandom=getRanks(choices(Cards,k=4))
    if len(set(listRandom).intersection({'J','Q','K'}))==0:
      count+=1
  return count/n

def experiment_f(n):
  count=0
  for _ in range(n):
    listRandom=getRanks(choices(Cards,k=4))
    print(listRandom)
    if len(set(listRandom).intersection({'J','Q','K'}))==4:
      count+=1
  return count/n

def main():
  n=10
  print('a/ All 4 cards are from the same suit. ',experiment_a(n))
  print('b/ All 4 cards are differents suits. ',experiment_b(n))
  print('c/ All 4 cards are same color. ',experiment_c(n))
  print('d/ All 4 cards are same value. ',experiment_d(n))
  print('e/ All 4 cards are numbers. ',experiment_e(n))
  print('f/ All 4 cards are faces. ',experiment_f(n))

if __name__ == '__main__':
  main()
