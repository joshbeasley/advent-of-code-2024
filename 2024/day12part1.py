res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def in_bounds(r, c):
  return r >= 0 and r < R and c >= 0 and c < C

def num_sides(r, c, plant):
  res = 0
  for x, y in directions:
    if not in_bounds(r+x, c+y) or grid[r+x][c+y] != plant:
      res += 1
  return res

seen = set()
def flood(r, c, plant):
  if not in_bounds(r, c) or grid[r][c] != plant or (r, c) in seen:
    return (0, 0)
  
  seen.add((r, c))
  res = (0, 0)
  for x, y in directions:
    area, perim = flood(r + x, c + y, plant)
    res = (res[0] + 1 + area, res[1] + num_sides(r, c, plant) + perim)
  return res

for r in range(R):
  for c in range(C):
    area, perim = flood(r, c, grid[r][c])
    area, perim = area // 4, perim // 4
    res += area * perim
    
print(res)
    