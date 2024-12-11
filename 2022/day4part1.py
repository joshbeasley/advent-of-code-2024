res = 0

def contains(pair1, pair2):
  x1, y1 = pair1
  x2, y2 = pair2
  
  return True if x1 <= x2 and y1 >= y2 else False

lines = open(0).readlines()

for line in lines:
  pair1, pair2 = line.strip().split(',')
  pair1 = list(map(int, pair1.split('-')))
  pair2 = list(map(int, pair2.split('-')))
  if contains(pair1, pair2) or contains(pair2, pair1):
    res += 1
    
print(res)
