from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        r = 1
        while r < len(nums):
            if nums[l] != 0:
                l += 1
            elif nums[r] != 0:
                (nums[l], nums[r]) = (nums[r], nums[l])
                l += 1
            r += 1

solution =  Solution()
list: List = [0, 1, 0, 3, 12]
# list: List = [1,0,1]
# list: List = [2,1]
solution.moveZeroes(list)
print(list)
