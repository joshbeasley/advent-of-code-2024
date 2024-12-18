import re

res = 0
for line in open(0).read().split('\n\n'):
  ax, ay, bx, by, px, py = map(int, re.findall(r"\d+", line))
  px, py = px + 10000000000000, py + 10000000000000
  sol_a = (px * by - py * bx) / (ax * by - ay * bx)
  sol_b = (px - ax * sol_a) / bx
  if sol_a % 1 == 0 and sol_b % 1 == 0:
    res += int(3 * sol_a + sol_b)

print(res)