def same_permutation(n):
	a = sorted(str(n))

	if a == sorted(str(2 * n)) and a == sorted(str(3 * n)) and a == sorted(str(4 * n)) and a == sorted(str(5 * n)) and a == sorted(str(6 * n)):
		return True
	return False

n = 1
while not same_permutation(n):
	n += 1

print n