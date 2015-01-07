MAX = 775148
candidates = {i for i in xrange(2, MAX)}

def sieve():
  for i in xrange(2, MAX):
    comp = i
    while comp < MAX:
      if i != comp:
        try:
          candidates.remove(comp)
        except:
          comp += i
          continue

#        print comp

      comp += i

  return candidates

a = sieve()
print len(a)

b = list(a)
c = sorted(b)
print c[10000]

