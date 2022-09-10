import itertools
list_ball=['w'+str(i) for i in range(8)]+['B'+str(i) for i in range(6)]+['R'+str(i) for i in range(9)]
#a

U3=list(itertools.combinations(list_ball, 3))
print(U3)
print(len(U3))
# #b
list_ball_2=[['w'+str(i) for i in range(8)], ['B'+str(i) for i in range(6)], ['R'+str(i) for i in range(9)]]
U3=list(itertools.product(*list_ball_2))
print(U3)
print(len(U3))
# #c

def cross_join(A,B):
  return {(a,b) for a in A for b in B }
list_ball_3=[['w'+str(i) for i in range(8)], ['R'+str(i) for i in range(6)]]
list_ball_3_b=[['B'+str(i) for i in range(9)]]

U3_wr=list(itertools.product(*list_ball_3))
U3_b=list(itertools.product(*list_ball_3_b))
U3_wr_b=cross_join(U3_wr,U3_b)
print(U3_wr_b)
print(len(U3_wr_b))




