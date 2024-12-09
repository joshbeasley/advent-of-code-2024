from collections import defaultdict
from itertools import combinations

res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])

antennas = defaultdict(list)

for r in range(R):
  for c in range(C):
    if grid[r][c] != '.':
      antennas[grid[r][c]].append([r, c])

def add_coords(coord1, coord2):
  return [coord1[0] + coord2[0], coord1[1] + coord2[1]]

def subtract_coords(coord1, coord2):
  return [coord1[0] - coord2[0], coord1[1] - coord2[1]]

def in_bounds(coord):
  return coord[0] >=0 and coord[0] < R and coord[1] >= 0 and coord[1] < C

def get_antinodes(ant1, ant2):
  diff = [ant1[0] - ant2[0], ant1[1] - ant2[1]]
  antinodes = [add_coords(ant1, diff), add_coords(ant2, diff), subtract_coords(ant1, diff), subtract_coords(ant2, diff)]
  return list(filter(lambda x: x != ant1 and x != ant2 and in_bounds(x), antinodes))

res = set()
for key, values in antennas.items():
  antenna_combos = list(combinations(values, 2))
  for ant1, ant2 in antenna_combos:
    antinodes = get_antinodes(ant1, ant2)
    for node in antinodes:
      res.add(tuple(node))


print(len(res))