print str(reduce(lambda a, b: a + b**b, range(1, 1001), 0))[-10:]