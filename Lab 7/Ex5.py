from itertools import *
from random import *
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
Cards = list(product(Ranks , Suits))


#Practical probability
dict_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, 'J':11, 'Q':12, 'K':13}
def get_value(card):
  return dict_values[card[0]]

def isStraight(cards):
  cards = sorted(list(map(get_value, cards)))
  for i in range(len(cards)-1):
    if cards[i+1] - cards[i] != 1:
      return False
  return True
  
def getCards():
  return choices(Cards, k=5)

def getProbability(n):
  count = 0
  for i in range(n):
    if isStraight(getCards()):
      count += 1
  return count / n

print(getProbability(1000))

#  Theorical probability

















