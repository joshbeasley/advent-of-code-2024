res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def is_xmas(r, c, d):
  for i, letter in enumerate("XMAS"):
    x = r + i * d[0]
    y = c + i * d[1]
    if x < 0 or x >= R or y < 0 or y >= C:
      return False
    if grid[x][y] != letter:
      return False
  return True

for r in range(R):
  for c in range(C):
    for direction in directions:
      res += is_xmas(r, c, direction)
    
  
print(res)