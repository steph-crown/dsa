from typing import List

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    n = len(nums)
    result = [1] * n

    agg = 1

    for i in range(len(nums)):
      result[i] *= agg
      agg *= nums[i]

    agg = 1

    for i in range(len(nums) - 1, -1, -1):
      result[i] *= agg
      agg *= nums[i]

    return result


solution = Solution()
print(solution.productExceptSelf([4,3,2,1,2]))
