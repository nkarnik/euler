multiples = []

for i in xrange(1000):
  if i % 3 == 0:
    multiples.append(i)
  elif i % 5 == 0:
    multiples.append(i)

print sum(multiples)
