from typing import List

class NumArray:
    nums = []
    prefix_sum = []

    def __init__(self, nums: List[int]):
      self.nums = nums

      for i in range(len(nums)):
        self.prefix_sum.insert(i, self.prefix_sum[i - 1] + nums[i] if i > 0 else nums[i])

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right] - self.prefix_sum[left - 1] if left > 0 else self.prefix_sum[right]




# Your NumArray object will be instantiated and called as such:
nums = [-1]
obj = NumArray(nums)
param_1 = obj.sumRange(0,0)
print(param_1)
