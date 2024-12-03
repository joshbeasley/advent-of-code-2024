import re

res = 0
text =  open(0).read()
muls = re.findall(r"mul\(\d{1,3},\d{1,3}\)", text)

for mul in muls:
  x, y = re.findall(r"\d{1,3},\d{1,3}", mul)[0].split(',')
  res += int(x) * int(y)
  
print(res)