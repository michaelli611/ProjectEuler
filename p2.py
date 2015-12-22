def fib_list(a, b, max, lst):
	if (a + b < max):
		lst.append(a + b)
		return fib_list(b, a + b, max, lst)
	else:
		return lst


print sum(filter(lambda x: x%2 == 0, fib_list(1, 2, 4000000, [1, 2])))
