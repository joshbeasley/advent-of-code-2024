curr = 50
count = 0

for i, line in enumerate(open(0)):
    dir, mag = line[0], int(line[1:])
    if dir == 'L':
        new = (curr - mag) % 100
        if curr != 0 and curr - mag <= 0:
            count += 1
            print(i, 'hit L')
    elif dir == 'R':
        new = (curr + mag) % 100
        if curr + mag >= 100:
            count += 1
            print(i, 'hit R')

    curr = new

    count += mag // 100

print(count)

