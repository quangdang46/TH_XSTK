from fractions import *

def P(event, space):
  return Fraction(len(event & space), len(space))

# a
S = {'MMM', 'MMF', 'MFM', 'MFF', 'FMM', 'FMF', 'FFM', 'FFF'}
# b
print(len(S))
# c
B={ s for s in S if 'F' in s}
# d
A_B = {s for s in B if s.count('F')==3}
# e
P_B = P(B, S)
P_A_B = P(A_B, S)
P_A_with_B = P_A_B/P_B
print(P_A_with_B)
