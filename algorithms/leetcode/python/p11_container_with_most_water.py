from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        m, l, r = 0, 0, len(height) - 1

        while r > l:
            l_val, r_val = height[l], height[r]
            a = (r - l) * min(l_val, r_val)
            m = max(m, a)

            print(f"l: {l}, r: {r}, l_val: {l_val}, r_val: {r_val}, m: {m}, a: {a}")

            l = l + 1 if l_val <= r_val else l
            r = r - 1 if r_val < l_val else r

        return m

solution: Solution = Solution()
print(solution.maxArea([1,2,3,1,4]))
# print(solution.maxArea([1,8,6,2,5,4,8,3,7]))
# print(solution.maxArea([1,2,1]))
