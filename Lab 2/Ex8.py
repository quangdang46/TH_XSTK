from fractions import Fraction
from itertools import *
from random import *
# tinh khong gian mau
def P(event , space):
  return Fraction(len(event & space), len(space))
# ket hop bong
def cross(A, B):
  return {a + b for a in A for b in B}
# chon n phan tu
def combos(items , n):
  return {' '.join(combo) for combo in combinations(items , n)}
urn = cross('W', '12345678') | cross('B', '123456') | cross(
'R', '123456789')
# print(urn.__len__())
# print(urn)
U=combos(urn, 6)

def solve():
  event = {combo for combo in U if combo.count('W') == 2
            and combo.count('B') == 2 
            and combo.count('R') == 2}
  return P(event, U)

print(solve())