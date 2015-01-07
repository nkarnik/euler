
MAX = 4000000

def fib():

  f1 = 1
  f2 = 2
  total = 2
  evens = []

  while f1 < MAX and f2 < MAX:
    fn = f1 + f2
    if fn % 2 == 0:
      total += fn
    evens.append(fn)

    if f1 < f2:
      f1 = fn
    else:
      f2 = fn

  return total, evens

print fib()    

