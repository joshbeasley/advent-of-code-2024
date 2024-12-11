list1 = []
list2 = []

for line in open(0).readlines():
  x, y = line.split()
  list1.append(x)
  list2.append(y)
  
list1.sort()
list2.sort()

res = 0
for i in range(len(list1)):
  res += abs(int(list1[i]) - int(list2[i]))
  
print(res)