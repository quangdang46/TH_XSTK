from itertools import *
from random import *


def cross(a, b):
  return [s+t for s in a for t in b]

urn=cross('B','12')+ cross('R','123') + cross('W','12345')

def format(arr):
  return set("".join([x[0] for x in arr]))

def format_2(arr):
  return "".join([x[0] for x in arr])

def experiment_a(n):
  count=0
  for _ in range(n):
    listRandom=format(choices(urn,k=3))
    if len(listRandom)==1:
      count+=1
  return count/n

def experiment_b(n):
  count=0
  for _ in range(n):
    listRandom=format(choices(urn,k=3))
    if len(listRandom)==3:
      count+=1
  return count/n

def experiment_c(n):
  count=0
  for _ in range(n):
    listRandom=format(choices(urn,k=3))
    if len(listRandom)==2:
      count+=1
  return count/n

def experiment_d(n):
  count=0
  for _ in range(n):
    listRandom=format_2(choices(urn,k=3))
    if listRandom.count('R')==2 and listRandom.count('W')==1:
      count+=1
  return count/n

def experiment_e(n):
  count=0
  for _ in range(n):
    listRandom=format_2(choices(urn,k=3))
    if listRandom.count('W')==3:
      count+=1
  return count/n

def main():
  n=100000
  print("a/ All 3 balls are same color: ", experiment_a(n))
  print("b/ All 3 balls are different colors: ", experiment_b(n))
  print("c/ Only 2 balls are same color: ", experiment_c(n))
  print("d/ There are 2 red balls and 1 white ball: ", experiment_d(n))
  print("e/ List all the cases that all 3 balls are white: ", experiment_e(n))

if __name__ == '__main__':
  main()


