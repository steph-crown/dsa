from typing import List

class Solution:
  def maxProduct(self, nums: List[int]) -> int:
    max_prod = max(nums)
    curr_max = 1
    curr_min = 1

    for num in nums:
      if num == 0:
        curr_max = 1
        curr_min = 1

      candidates = (num, curr_max * num, curr_min * num)
      curr_max, curr_min = max(candidates), min(candidates)
      max_prod = max(max_prod, curr_max)

    return max_prod

solution = Solution()
print(solution.maxProduct([-1,0,-2,2]))

#     print(f"product_after_first: {product_after_first}, product_before_last: {product_before_last}")
#     print(negs)
