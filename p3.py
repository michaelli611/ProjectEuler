import math

def prime_list(n):

	lst = [True] * n

	lst[0] = False
	lst[1] = False

	for x in range(2, int(math.ceil(math.sqrt(n)))):

		if lst[x] == True:
			j = 2 * x

			while j < n:
				lst[j] = False
				j += x


	primes = []

	for x in range(n):
		if lst[x] == True:
			primes.append(x)

	return primes


p = prime_list(int(math.sqrt(600851475143)))
n = 600851475143

for x in p:
	if n % x == 0:
		n /= x
		print x