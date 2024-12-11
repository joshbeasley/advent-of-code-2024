from collections import defaultdict

res = 0

def priority(char):
  if char.islower():
    return ord(char) - ord('a') + 1
  else:
    return ord(char) - ord('A') + 27

lines = open(0).readlines()

for i in range(0, len(lines), 3):
  items = set(list(lines[i])).intersection(set(list(lines[i+1])))
  for char in lines[i + 2]:
    if char in items:
      res += priority(char)
      break
print(res)