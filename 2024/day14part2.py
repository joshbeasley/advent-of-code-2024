import re
from math import prod

lines = open(0).readlines()
WIDTH = 101
HEIGHT = 103
min_sf = float('inf')
min_second = 0
robots = []

for line in lines:
  robots.append(tuple(map(int, re.findall(r"-?\d+", line))))

for second in range(WIDTH * HEIGHT):
  locations = []
  
  for x, y, dx, dy in robots:
    nx = (x + dx * second) % WIDTH
    ny = (y + dy * second) % HEIGHT
    locations.append((nx, ny))

  quadrants = [0, 0, 0, 0]
  for x, y in locations:
    if x < WIDTH // 2 and y < HEIGHT // 2:
      quadrants[0] += 1
    elif x > WIDTH // 2 and y < HEIGHT // 2:
      quadrants[1] += 1
    elif x > WIDTH // 2 and y > HEIGHT // 2:
      quadrants[2] += 1
    elif x < WIDTH // 2 and y > HEIGHT // 2:
      quadrants[3] += 1
  sf = prod(quadrants)

  if sf < min_sf:
    min_sf = sf
    min_second = second

print(min_sf, min_second)
  
    