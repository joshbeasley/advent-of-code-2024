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
direction = 0
visited = set()
while True:
  next_r, next_c = r + directions[direction][0], c + directions[direction][1]
  if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C:
    visited.add((r, c))
    break
  if grid[next_r][next_c] == '#':
    direction = (direction + 1) % 4
  
  if (r, c) not in visited:
    visited.add((r, c))
  
  r, c = r + directions[direction][0], c + directions[direction][1]

def is_cycle(obstacle_r, obstacle_c):
  grid[obstacle_r][obstacle_c] = '#'
  r, c = start
  direction = 0
  visited = set()
  visited_with_direction = set()

  while True:
    next_r, next_c = r + directions[direction][0], c + directions[direction][1]
    if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C:
      visited.add((r, c))
      grid[obstacle_r][obstacle_c] = '.'
      return False
      break
    
    if grid[next_r][next_c] == '#':
      direction = (direction + 1) % 4
      
    if (r, c, direction) in visited_with_direction:
      grid[obstacle_r][obstacle_c] = '.'
      return True
    
    if (r, c) not in visited:
      visited.add((r, c))
      visited_with_direction.add((r, c, direction))
      
    r, c = r + directions[direction][0], c + directions[direction][1]

res = 0
for r, c in visited:
  if is_cycle(r, c):
    res += 1

print(res)
