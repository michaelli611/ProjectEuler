import math

def num_divisors(n):
	sum = 0
	for x in range(1, int(math.sqrt(n)) + 1):
		if n % x == 0:
			sum += 2
	if math.sqrt(n)**2 == n:
		sum -= 1
	return sum

n = 1
while num_divisors(n * (n + 1)/2) < 500:
	n += 1

print n
