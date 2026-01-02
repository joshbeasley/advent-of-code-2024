import heapq

res = 0
lines =  open(0).readlines()
grid = [list(map(int, line.strip())) for line in lines]
R, C = len(grid), len(grid[0])

for row in grid:
    first = heapq.nlargest(1, enumerate(row), key=lambda x: x[1])
    if first[0][0] == len(row) - 1:
        first = heapq.nlargest(1, enumerate(row[:-1]), key=lambda x: x[1])

    second = heapq.nlargest(1, enumerate(row[first[0][0] + 1:]), key=lambda x: x[1])
    res += first[0][1] * 10 + second[0][1]

print(res)
    