res = 0
grid, moves =  open(0).read().split('\n\n')
grid = [list(line.strip()) for line in grid.split('\n')]
R, C = len(grid), len(grid[0])
moves = list(''.join(moves.split('\n')))
robot = None
move_map = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

for r in range(R):
  for c in range(C):
    if grid[r][c] == '@':
      robot = (r, c)

def print_grid():
  for row in grid:
    print(''.join(row))

def in_bounds(r, c):
  return r >= 0 and r < R and c >= 0 and c < C

def is_wall(r, c):
  return True if grid[r][c] == '#' else False

def is_empty(r, c):
  return True if grid[r][c] == '.' else False

def move_box(r, c, dr, dc):
  should_print = False
  if (r, c) == (1, 3):
    should_print = True
    print('hit')
  nr, nc = r + dr, c + dc
  num_blocks = 0
  while in_bounds(nr, nc) and grid[nr][nc] == 'O':
    num_blocks += 1
    nr, nc = nr + dr, nc + dc
  
  if not in_bounds(nr, nc) or grid[nr][nc] == '#':
    return (r, c)
  
  for i in range(num_blocks):
    grid[nr][nc] = 'O'
    nr, nc = nr - dr, nc - dc
  
  return (nr, nc)
  

def execute_move(robot, move):
  r, c = robot
  dr, dc = move_map[move]
  if not in_bounds(r + dr, c + dc):
    return robot
  if is_wall(r + dr, c + dc):
    return robot
  if is_empty(r + dr, c + dc):
    return (r + dr, c + dc)
  
  return move_box(r, c, dr, dc)
  
for move in moves:
  old_pos = robot
  robot = execute_move(robot, move)
  grid[old_pos[0]][old_pos[1]] = '.'
  grid[robot[0]][robot[1]] = '@'

res = 0
for r in range(R):
  for c in range(C):
    if grid[r][c] == 'O':
      res += 100 * r + c

print(res)
