res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
seen = set()

def in_bounds(r, c):
  return r >= 0 and r < R and c >= 0 and c < C

def dfs(r, c, num):
  if not in_bounds(r, c) or grid[r][c] != str(num):
    return 0
  
  if num == 9 and (r, c) not in seen:
    seen.add((r, c))
    return 1
  
  res = 0  
  for a, b in directions:
    res += dfs(r + a, c + b, num + 1)
  
  return res

for r in range(R):
  for c in range(C):
    res += dfs(r, c, 0)
    seen.clear()
    
print(res)