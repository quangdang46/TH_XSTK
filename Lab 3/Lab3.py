from fractions import *
from itertools import *
from random import *

# ex1
def P(event, space):
  return Fraction(len(event), len(space))

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

# ex2
S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'),
      ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'),
      ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), 
      ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'),
      ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]

# a
A={ s for s in S if s[0] == 'Thanh'}
# b
B={ s for s in S if s[1] == 'Nữ'}
# c
A_B = {s for s in B if s[0] == 'Thanh'}


# d
P_A = P(A, S)
print(P_A)

P_B = P(B, S)
print(P_B)

P_A_B = P(A_B, S)
print(P_A_B)
# e

P_A_with_B = P_A_B/P_B
print(P_A_with_B)

# ex3
Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'♡', '♢', '♣', '♠'}
# '♡', '♢': red
# '♣', '♠': black

# a
Cards =set(map(lambda x:str(x[0])+x[1], product(Ranks, Suits)))
# print(Cards)

# b

B = list(permutations(Cards, 3))
# print(B)

# c
A1 = set(filter(lambda x: x.count('K') in {1, 2},list(map(lambda x: ''.join(x), list(permutations(Cards, 3))))))
# print(A1)

# d
A2 = set(filter(lambda x: x.count('K')>=1,list(map(lambda x: ''.join(x), list(permutations(Cards, 3))))))
print(round(P(A1, B),4))
print(round(P(A2, B),4))