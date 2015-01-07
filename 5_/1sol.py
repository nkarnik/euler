factors = [i for i in xrange(11,21)]
mult = 1
for f in factors:
  mult *= f

print factors
print mult
smallest = 0

for a in xrange(21, mult):
  for f in factors:
    invalid = False
    if a % f != 0:
      #print a
      invalid = True
      break
  if invalid:
    continue

  else:
    smallest = a
    print smallest
    break
    

print smallest
