
def isPalindrome(num):
  s = str(num)
  spl = [i for i in s]

  size = len(spl)
  middle = size / 2
  opp = 0
  if size % 2 == 0:
    opp = middle - 1
  else:
    middle += 1
    opp = middle - 2

  pal = False

  while middle < size:
    if spl[middle] == spl[opp]:
      middle += 1
      opp -= 1

    else:
      return pal

  pal = True
  return pal
    
  
print isPalindrome(90109)

largest = 0
for i in xrange(1000):
  for j in xrange(1000):
    prod = i*j
    if isPalindrome(prod):
      if prod > largest:
        largest = prod

print largest
