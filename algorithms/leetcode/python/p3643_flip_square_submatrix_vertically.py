from typing import List

class Solution:
  def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
    i, j = x, x + k - 1

    while i < j:
      print(f"i {i}, j {j}")
      grid[i][y:y+k], grid[j][y:y+k] = grid[j][y:y+k], grid[i][y:y+k]
      i+=1
      j-=1

    return grid

solution = Solution()
print(solution.reverseSubmatrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 1, 0, 3))
