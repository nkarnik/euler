sln = 0
NUM = 600851475143
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

def mprime(a):
  m = -1
  for prime in a:
    if NUM % prime == 0 and prime > m:
      print prime
      m = prime

  return m

print mprime(a)

