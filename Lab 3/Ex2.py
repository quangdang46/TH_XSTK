from fractions import *


def P(event, space):
  return Fraction(len(event), len(space))

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


