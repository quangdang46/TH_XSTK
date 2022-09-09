import itertools
U3=list(itertools.permutations([['M']*4, ['P']*3, ['C']*2, ['L']*1], 4))
for i in range(len(U3)):
  U3[i]=list(U3[i])
  U3[i]=list(itertools.chain(*U3[i]))
print(U3)
print(U3.__len__())



