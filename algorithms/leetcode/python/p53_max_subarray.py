from typing import List
# kadane's algo
class Solution:
  def maxSubArray(self, nums: List[int]) -> int:
    max_sum = nums[0]
    curr_sum = nums[0]

    for i in range(1, len(nums)):
      curr_sum = max(nums[i], nums[i] + curr_sum)
      max_sum = max(curr_sum, max_sum)

    return max_sum


solution = Solution()
print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
