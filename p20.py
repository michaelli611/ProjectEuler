n = reduce(lambda a, b: a * b, range(1, 101), 1)

sum = 0

while n >= 1:
	sum += n % 10
	n /= 10

print sum