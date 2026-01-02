import heapq

res = 0
lines =  open(0).readlines()
grid = [list(map(int, line.strip())) for line in lines]
R, C = len(grid), len(grid[0])


for row in grid:
    start, end = 0, len(row) - 11
    size = 100000000000
    total = 0
    index_addition = 1
    for _ in range(12):
        num = heapq.nlargest(1, enumerate(row[start:end]), key=lambda x: x[1])
        res += num[0][1] * size
        total += num[0][1] * size
        size /= 10
        start = num[0][0] + index_addition
        index_addition += num[0][0] + 1
        end += 1
print(res)