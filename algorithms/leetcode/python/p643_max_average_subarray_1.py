from typing import List

class Solution:
  def findMaxAverage(self, nums: List[int], k: int) -> float:
    max_total = 0

    for i in range(k):
      max_total += nums[i]

    l, r, curr_total = 1, k, max_total

    while r < len(nums):
      curr_total = curr_total - nums[l - 1] + nums[r]
      max_total = max(curr_total, max_total)
      l += 1
      r += 1

    return round(max_total / k, 5)

solution: Solution = Solution()
print(solution.findMaxAverage([4,2,1,3,3], 2))
