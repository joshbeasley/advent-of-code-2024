from copy import deepcopy

res = 0
lines =  open(0).readlines()
grid = [list(line.strip()) for line in lines]
R, C = len(grid), len(grid[0])
directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# grid_copy = deepcopy(grid)

def is_roll(r, c):
    return grid[r][c] == '@'

def is_valid(r, c):
    return r < R and r >= 0 and c < C and c >= 0

def print_grid(grid):
    res = ''
    for r in range(R):
        res += ''.join(grid[r])
        res += '\n'
    print(res)

for r in range(R):
    for c in range(C):
        if is_roll(r, c):
            rolls = 0
            for a, b in directions:
                if is_valid(r + a, c + b) and is_roll(r + a, c + b):
                    rolls += 1
            if rolls < 4:
                # grid_copy[r][c] = 'x'
                res += 1

# print_grid(grid_copy)
print(res)
