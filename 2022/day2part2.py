def score(p1, p2):
  p1 = ord(p1) - ord('A')

  if p2 == 'X':
    return (p1 - 1) % 3 + 1
  elif p2 == 'Y':
    return 3 + p1 + 1
  else:
    return 6 + (p1 + 1) % 3 + 1
  
res = 0
for line in open(0).readlines():
  p1, p2 = line.split()
  res += score(p1, p2)

print(res)