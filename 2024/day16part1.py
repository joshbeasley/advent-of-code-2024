from collections import defaultdict
from queue import PriorityQueue

res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions
source = None
dest = None

def get_neighbors(node):
  r, c = node
  neighbors = []
  
# TODO: need to keep track of current direction somehow

dist = defaultdict(lambda: float('inf'))
prev = {}
Q = set()

for r in range(R):
  for c in range(C):
    if grid[r][c] == 'S':
      source = (r, c)
    if grid[r][c] == 'E':
      dest = (r, c)
    prev[(r, c)] = None
    dist[(r, c)] = float('inf')
    Q.add((r, c))
dist[source] = 0

while not Q.empty():
  u = min(d, key=dist.get)
  Q.remove(u)
  for v, weight in get_neighbors(u):
    alt = dist[u] + weight
    if alt < dist[v]:
      prev[v] = u
      dist[v] = alt
  
