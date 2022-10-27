from random import *

def rollDice():
  return randint(1,6)

def rollTwoDice_a(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1 == d2:
      count += 1
  return count/n

def rollTwoDice_b(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1 != d2:
      count += 1
  return count/n

def rollTwoDice_c(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1%2 == 0 and d2%2 == 0:
      count += 1
  return count/n

def rollTwoDice_d(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1%2 == 1 and d2%2 == 1:
      count += 1
  return count/n

def rollTwoDice_e(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1%2 == 1 and d2%2 == 0 or d1%2 == 0 and d2%2 == 1:
      count += 1
  return count/n

def rollTwoDice_f(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1 == 6 and d2 == 6:
      count += 1
  return count/n

def rollTwoDice_g(n):
  count = 0
  for i in range(n):
    d1 = rollDice()
    d2 = rollDice()
    if d1 + d2 > 10:
      count += 1
  return count/n

n=1000
print("a/ Both dice are the same: ", rollTwoDice_a(n))
print("b/ Both dice are different: ", rollTwoDice_b(n))
print("c/ Both dice are even: ", rollTwoDice_c(n))
print("d/ Both dice are odd: ", rollTwoDice_d(n))
print("e/ One die is even and the other is odd: ", rollTwoDice_e(n))
print("f/ Both dice are 6: ", rollTwoDice_f(n))
print("g/ Summation of both dice are greater than 10: ", rollTwoDice_g(n))


