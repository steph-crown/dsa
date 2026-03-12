from typing import List
from collections import Counter

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    count = Counter(nums)
    return [num for num, _ in count.most_common(k)]

solution = Solution()
print(solution.topKFrequent([3,0,1,0], 2))
