res = 0

def overlap(pair1, pair2):
  x1, y1 = pair1
  x2, y2 = pair2
  
  return False if x2 > y1 or x1 > y2 else True

lines = open(0).readlines()

for line in lines:
  pair1, pair2 = line.strip().split(',')
  pair1 = list(map(int, pair1.split('-')))
  pair2 = list(map(int, pair2.split('-')))
  if overlap(pair1, pair2):
    res += 1
    
print(res)
