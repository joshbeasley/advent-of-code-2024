from itertools import product

def can_solve(target, nums):
  if len(nums) == 1:
    return nums[0] == target
  if target % nums[-1] == 0 and can_solve(target // nums[-1], nums[:-1]):
    return True
  if target > nums[-1] and can_solve(target - nums[-1], nums[:-1]):
    return True
  return False
    

res = 0

for line in open(0).readlines():
  target, nums = line.split(':')
  target = int(target)
  nums = list(map(int, nums.split()))
  if can_solve(target, nums):
    res += target
    
print(res)
