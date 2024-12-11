
res = 0
disk = list(str(open(0).read()).strip())

blocks = []
file_id = 0
for i, char in enumerate(disk):
  char = int(char)
  if i % 2 == 0:
    blocks += [file_id] * char
    file_id += 1
  else:
    blocks += [-1] * char

blanks = [i for i, v in enumerate(blocks) if v == -1]

for i in blanks:
  while blocks[-1] == -1:
    blocks.pop()
  if len(blocks) <= i:
    break
  blocks[i] = blocks.pop()

print(sum(i * v for i, v in enumerate(blocks)))