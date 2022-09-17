# Ex1
import itertools
A = {i for i in range(10)}
num_code = []
for i in itertools.permutations(A, 4):
	num_code.append(int("".join(map(str, i))))
code_length=num_code.__len__()
print("Cac so 4 chu so co the tao ra tu cac chu so trong tap A la: ", num_code)
print("So luong cac so 4 chu so co the tao ra tu cac chu so trong tap A la: ", code_length)