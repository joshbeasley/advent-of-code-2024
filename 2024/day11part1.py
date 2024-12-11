res = 0
nums =  open(0).read().split()

def remove_leading_zeros(num):
  return str(int(num))

def dfs(num, depth):
  if depth == 25:
    return 1
  
  num = remove_leading_zeros(num)
  
  if num == '0':
    return dfs('1', depth + 1)
  
  if len(num) % 2 == 0:
    mid = len(num) // 2
    return dfs(num[:mid], depth + 1) + dfs(num[mid:], depth + 1)
  
  return dfs(str(int(num) * 2024), depth + 1)

for num in nums:
  res += dfs(num, 0)
  
print(res)