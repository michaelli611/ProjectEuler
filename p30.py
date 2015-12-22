def sum_fifth_power(n):
	sum = 0

	while n > 0:
		sum += (n % 10) ** 5
		n /= 10

	return sum


print reduce(lambda a, b: a + b if (sum_fifth_power(b) == b) else a, range(10, 1000000), 0)