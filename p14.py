def collatz_chain_lst(n, lst):
	if n == 1:
		return 1
	elif n%2 == 0:
		return collatz_chain(n/2) + 1
	else:
		return collatz_chain(3*n + 1) + 1

print collatz_chain(13, [99999999] * 14)

max = 0
n = 0

for x in range(1000001):
	
	c = x

	j = 0

	while c > 1:
		if c % 2 == 0:
			c /= 2
		else:
			c = 3 * c + 1
		j += 1



	if max < j:
		max = j
		n = x

print n