
res = 0
disk = list(str(open(0).read()).strip())

fid = 0
pos = 0
files = {}
blanks = []
for i, num in enumerate(disk):
  num = int(num)
  if i % 2 == 0:
    files[fid] = (pos, num)
    fid += 1
  else:
    if num != 0:
      blanks.append((pos, num))
  pos += num

while fid > 0:
  fid -= 1
  pos, size = files[fid]
  for i, (start, length) in enumerate(blanks):
    if start >= pos:
      blanks = blanks[:i]
      break
    if size <= length:
      files[fid] = (start, size)
      if size == length:
        blanks.pop(i)
      else:
        blanks[i] = (start + size, length - size)
      break
      
for fid, (pos, size) in files.items():
  for i in range(pos, pos + size):
    res += fid * i
    
print(res)