from collections import defaultdict

lines = open(0).readlines()

x = 0
while not lines[x][1].isdigit(): x += 1

num_stacks = int(lines[x].strip()[-1])
stacks = defaultdict(list)
for i in range(x - 1, -1, -1):
  stack_num = 1
  for j in range(1, (num_stacks - 1) * 4 + 2, 4):
    if lines[i][j] != ' ':
      stacks[stack_num].append(lines[i][j])
    stack_num += 1

moves = []
for i in range(x + 2, len(lines)):
  line = lines[i].strip().split(' ')
  moves.append((int(line[1]), int(line[3]), int(line[5])))

for move in moves:
  for i in range(move[0]):
    block = stacks[move[1]].pop()
    stacks[move[2]].append(block)

res = ''
for i, stack in stacks.items():
  res += stack[-1]

print(res)