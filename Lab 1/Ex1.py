import itertools
A = {1, 2, 3, 4, 5}
num_3_digit = []
for i in itertools.permutations(A, 3):
	num_3_digit.append(int("".join(map(str, i))))
print("Cac so 3 chu so co the tao ra tu cac chu so trong tap A la: ", num_3_digit)
print("So luong cac so 3 chu so co the tao ra tu cac chu so trong tap A la: ", len(num_3_digit))
