import random
import math


def flip():
  return random.randint(0,1)

def count(arr,check=1):
  return arr.count(check)

def init(times):
  return [count([flip(),flip()]) for i in range(times)]

x = init(3)
print(x)

# b
X=set(x)
# print(X)

# c
P=[x.count(i)/len(x) for i in X]
# print(P)

# d

# Kỳ vọng
EX=0
for x in X:
  EX+=x*P[x-1]
# print(EX)

# Phương sai
VarX=0
for x in X:
  VarX+=(x-EX)**2*P[x-1]
# print(VarX)

# Độ lệch chuẩn
SD=math.sqrt(VarX)
# print(SD)

#e

print(sum(P[1:]))


  








