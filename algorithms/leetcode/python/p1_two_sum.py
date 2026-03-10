from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      num_idxs = {}

      for i in range(len(nums)):
        num_idxs[nums[i]] = i

      print(num_idxs)

      for i in range(len(nums)):
        comp = target - nums[i]

        if comp in num_idxs:
            idx = num_idxs[comp]
            if idx == i:
              continue
            return [idx, i]
      return []

solution = Solution()
print(solution.twoSum([3,3], 6))
