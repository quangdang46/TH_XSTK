import itertools
list_ball=['w'+str(i) for i in range(8)]+['B'+str(i) for i in range(6)]+['R'+str(i) for i in range(9)]
#a

U2=list(itertools.combinations(list_ball, 3))
print(U2)
print(len(U2))
# #b
list_ball_2=[['w'+str(i) for i in range(8)], ['B'+str(i) for i in range(6)], ['R'+str(i) for i in range(9)]]
U2=list(itertools.product(*list_ball_2))
print(U2)
print(len(U2))
# #c

U2_wrb=list(itertools.permutations(list_ball, 3))
def check(arr):
  return arr[0][0] =='w' and arr[1][0]=='R'
result=list(filter(check, U2_wrb))
print(len(result))
print(result)
