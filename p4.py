import math

def is_palindrome(n):
	s = str(n)

	if s[:len(s)/2:][::-1] == s[int(math.ceil(len(s)/2.0)):]:
		return True
	return False

max = 0

for x in range(100, 1000):
	for y in range(100, 1000):
		if is_palindrome(x*y) and x*y > max:
			max = x*y

print max


