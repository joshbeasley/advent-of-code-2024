curr = 50
count = 0

for i, line in enumerate(open(0)):
    dir, mag = line[0], int(line[1:])
    if dir == 'L':
        curr = (curr - mag) % 100
    elif dir == 'R':
        curr = (curr + mag) % 100
    
    if curr == 0:
        count += 1

print(count)

