res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

def is_x_mas(r, c):
  if r < 1 or r >= R - 1 or c < 1 or c >= C - 1:
    return False
  
  if grid[r][c] != "A":
    return False
  
  diag1 = f"{grid[r+1][c+1]}{grid[r-1][c-1]}"
  diag2 = f"{grid[r+1][c-1]}{grid[r-1][c+1]}"
  
  if diag1 in ["MS", "SM"] and diag2 in ["MS", "SM"]:
    return True
  return False

for r in range(R):
  for c in range(C):
    res += is_x_mas(r, c)
    
  
print(res)