from typing import List

class Solution:
  def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
    rows, cols = len(grid), len(grid[0])
    p = [[0] * (cols + 1) for _ in range(rows + 1)]
    count = 0

    for r in range(1, rows + 1):
      for c in range(1, cols + 1):
        p[r][c] = grid[r - 1][c - 1] + p[r - 1][c] + p[r][c - 1] - p[r - 1][c - 1]
        if p[r][c] <= k:
          count += 1
        else:
          break

    return count


solution = Solution()
print(solution.countSubmatrices([[7,6,3],[6,6,1]], 18))
print(solution.countSubmatrices([[7,2,9],[1,5,0],[2,6,6]], 20))

"""
[0 0   0   0]
[0 7   13  16]
[0 13. 25. 29]
"""
