ranges = open(0).read().split(',')
output = 0

for item in ranges:
    first, last = item.split('-')
    first, last = int(first), int(last)
    for i in range(first, last + 1):
        num = str(i)
        num_len = len(num)
        for j in range(2, num_len + 1):
            if num_len % j == 0 and num[:num_len // j] * j == num:
                output += int(num)
                break

print(output)


