import itertools
#a
U3=list(itertools.combinations_with_replacement(['W', 'B', 'R'], 3))
print(U3)
print(len(U3))
#b
U3=list(itertools.combinations(['W', 'B', 'R'], 3))
print(U3)
print(len(U3))
#c
U3=list(itertools.combinations(['W', 'R'], 2))
for i in range(len(U3)):
  U3[i]=list(U3[i])
  U3[i].append('B')
print(U3)
print(len(U3))
