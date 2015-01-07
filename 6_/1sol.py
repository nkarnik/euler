

def sumsq(r):
  s = 0
  for i in xrange(r):
    s += i*i

  return s

def sqsum(r):

  s = 0
  for i in xrange(r):
    s += i

  return s*s

print sqsum(101) - sumsq(101)
