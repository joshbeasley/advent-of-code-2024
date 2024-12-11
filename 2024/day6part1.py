res = 2
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# find starting position
start = None
for i, row in enumerate(grid):
  if '^' in row:
    start = (i, grid[i].index('^'))

r, c = start
grid[r][c] = 'X'
direction = 0
while True:
  next_r, next_c = r + directions[direction][0], c + directions[direction][1]
  if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C:
    break
  if grid[next_r][next_c] == '#':
    direction = (direction + 1) % 4
  
  if grid[r][c] == '.':
    grid[r][c] = 'X'
    res += 1
  
  r, c = r + directions[direction][0], c + directions[direction][1]

print(res)