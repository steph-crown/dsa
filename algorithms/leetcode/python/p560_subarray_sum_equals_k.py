from typing import List
from collections import Counter

class Solution:
  def subarraySum(self, nums: List[int], k: int) -> int:
    for i in range(1, len(nums)):
      nums[i] = nums[i] + nums[i - 1]

    count = 0
    occ = Counter({0: 1})
    for j in range(len(nums)):
      l_val = nums[j] - k
      count += occ.get(l_val, 0)
      occ[nums[j]] += 1

    return count

solution = Solution()
print(solution.subarraySum([1,2,1,2,2,3],4))
