res = 0

def priority(char):
  if char.islower():
    return ord(char) - ord('a') + 1
  else:
    return ord(char) - ord('A') + 27

for line in open(0).readlines():
  items = set(list(line[:len(line) // 2]))
  for i in range(len(line) // 2, len(line)):
    if line[i] in items:
      res += priority(line[i])
      break

print(res)