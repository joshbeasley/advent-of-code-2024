def score(p1, p2):
  p1 = ord(p1) - ord('A')
  p2 = ord(p2) - ord('X')
  if p1 == p2:
    return 3 + p2 + 1
  elif (p1 - p2) % 3 == 1:
    return 6 + p2 + 1
  else:
    return 0 + p2 + 1
  
res = 0
for line in open(0).readlines():
  p1, p2 = line.split()
  res += score(p1, p2)

print(res)







