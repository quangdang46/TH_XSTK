from random import *
import math

x=[randint(1,6) for i in range(8000)]
X=set(x)
# print(X)
# print(x)

P=[x.count(i)/len(x) for i in X]
print(P)

# Chức năng phân phối tích lũy
FX=sum(P[:3])
print(FX)

# Kỳ vọng
EX=0
for x in X:
  EX+=x*P[x-1]
print(EX)


# Phương sai
VarX=0
for x in X:
  VarX+=(x-EX)**2*P[x-1]
print(VarX)

# Độ lệch chuẩn
SD=math.sqrt(VarX)
print(SD)
# Điểm tiêu chuẩn