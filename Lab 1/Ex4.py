import itertools
def cross(A, B):
  return {a + b for a in A for b in B}
U4_men=list(itertools.combinations(['M1','M2','M3','M4','M5','M6'],3))
U4_women=list(itertools.combinations(['W1','W2','W3','W4','W5','W6','W7','W8','W9'],2))
U4=cross(U4_men,U4_women)
print(U4)
print(U4.__len__())
