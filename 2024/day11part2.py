res = 0
nums =  open(0).read().split()
memo = {}

def remove_leading_zeros(num):
  return str(int(num))

def cache(num, steps, res):
  memo[(num, steps)] = res

def dfs(num, steps):
  if steps == 0:
    return 1
  
  num = remove_leading_zeros(num)
  
  if (num, steps) in memo:
    return memo[(num, steps)]
  
  if num == '0':
    res = dfs('1', steps - 1)
    cache(num, steps, res)
    return res
    
  if len(num) % 2 == 0:
    mid = len(num) // 2
    res = dfs(num[:mid], steps - 1) + dfs(num[mid:], steps - 1)
    cache(num, steps, res)
    return res
  
  res = dfs(str(int(num) * 2024), steps - 1)
  cache(num, steps, res)
  return res

for num in nums:
  res += dfs(num, 75)
  
print(res)

