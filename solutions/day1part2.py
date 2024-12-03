from collections import defaultdict

list1 = []
list2 = []

for line in open(0).readlines():
  x, y = line.split()
  list1.append(x)
  list2.append(y)
  
counts = defaultdict(int)
for num in list2:
  counts[int(num)] += 1

res = 0
for num in list1:
  res += int(num) * counts[int(num)]
  
print(res)