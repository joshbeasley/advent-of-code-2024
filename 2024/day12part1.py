from collections import deque

def recursive_solution():
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
      
  # print(res)

def bfs_solution():
  res = 0
  file = open(0)
  lines =  file.readlines()
  grid = [list(line.strip()) for line in lines]
  R, C = len(grid), len(grid[0])
  directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

  def in_bounds(r, c):
    return r >= 0 and r < R and c >= 0 and c < C

  def num_sides(r, c):
    res = 0
    for x, y in directions:
      if not in_bounds(r+x, c+y) or grid[r+x][c+y] != grid[r][c]:
        res += 1
    return res
  
  seen = set()
  regions = []
  
  for r in range(R):
    for c in range(C):
      if (r, c) in seen: continue
      seen.add((r, c))
      region = set([(r, c)])
      plant = grid[r][c]
      q = deque([(r, c)])
      while q:
        cr, cc = q.popleft()
        for dr, dc in directions:
          nr, nc = cr + dr, cc + dc
          if not in_bounds(nr, nc) or grid[nr][nc] != plant or (nr, nc) in region: 
            continue
          region.add((nr, nc))
          seen.add((nr, nc))
          q.append((nr, nc))
      regions.append(region)
  
  def perimeter(region):
    perim = 0
    for r, c in region:
      perim += num_sides(r, c)
    return perim
    
  print(sum(perimeter(region) * len(region) for region in regions))
      
