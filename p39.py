p = [0]*1001

for a in range(1, 1000):
	for b in range(a, 1000):
		for c in range(b, 1000):
			if a + b + c > 1000:
				break
			elif a**2 + b**2 == c**2:
				p[a + b + c] += 1

print p.index(max(p))