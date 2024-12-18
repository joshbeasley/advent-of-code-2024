import re
from math import prod

WIDTH = 101
HEIGHT = 103

res = 0
locations = []
for line in open(0).readlines():
  x, y, dx, dy = map(int, re.findall(r"-?\d+", line))
  for i in range(100):
    x = (x + dx) % WIDTH
    y = (y + dy) % HEIGHT
  locations.append((x, y))

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

print(prod(quadrants))
  
    