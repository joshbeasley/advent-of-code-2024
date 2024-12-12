buffer = input()

last_four = []
for i in range(len(buffer)):
  last_four.append(buffer[i])
  if len(last_four) == 5:
    last_four.pop(0)
  if len(set(last_four)) == 4:
    print(i + 1)
    break