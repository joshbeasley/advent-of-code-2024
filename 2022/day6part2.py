buffer = input()

last_fourteen = []
for i in range(len(buffer)):
  last_fourteen.append(buffer[i])
  if len(last_fourteen) == 15:
    last_fourteen.pop(0)
  if len(set(last_fourteen)) == 14:
    print(i + 1)
    break