import sys
sys.setrecursionlimit(10000)

def fib_list(a, b, lst):
	if (len(str(a + b)) < 1000):
		lst.append(a + b)
		return fib_list(b, a + b, lst)
	else:
		return len(lst) + 1

print fib_list(1, 1, [1, 1])
