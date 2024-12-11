import re

res = 0
text =  open(0).read()
muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)|don't\(\)|do\(\)", text)

do = True
for mul in muls:
  if mul == 'do()':
    do = True
  elif mul == 'don\'t()':
    do = False
  elif do:
    x, y = re.findall(r"\d{1,3},\d{1,3}", mul)[0].split(',')
    res += int(x) * int(y)
  
print(res)