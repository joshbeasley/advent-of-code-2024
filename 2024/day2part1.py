def is_increasing(nums):
  for i in range(len(nums)-1):
    if nums[i+1] - nums[i] < 1 or nums[i+1] - nums[i] > 3:
      return False
  return True

def is_decreasing(nums):
  for i in range(len(nums)-1):
    if nums[i+1] - nums[i] > -1 or nums[i+1] - nums[i] < -3:
      return False
  return True


res = 0
for line in open(0).readlines():
  nums = [int(i) for i in line.split()]
  if is_increasing(nums) or is_decreasing(nums):
    res += 1
    
print(res)