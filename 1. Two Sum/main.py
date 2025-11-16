def twoSum(nums: list[int], target: int) -> list[int]:

  num = 0

  for n in nums:
    if n < target:
      num += target - n
    
  if num in nums:
    return [nums[num], nums[n]]
    
print(twoSum([15, 7, 2, 11], 9))
    
  
