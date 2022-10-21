import numpy as np

x=np.random.choice([0,1,2,3,4,5],size=3650,p=[0.1,0.2,0.3,0.2,0.15,0.05])

# print(x)

# a
X=set(x)

# b 

P=[x.tolist().count(i)/len(x) for i in X]
# print(P)


# c
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
import math
SD=math.sqrt(VarX)
# print(SD)

# d
print(sum(P[2:]))



