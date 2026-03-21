from typing import List
from pprint import pprint


class Solution:
  def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
    # nested loop
    # track number of xs and ys and count of submatrices
    # (x,y)
    # create prefix sum array to track counts of (x,y)
    # during the process, you'll know the one that passes condition and add it.
    rows, cols = len(grid), len(grid[0])
    p = [[(0,0)] * (cols + 1) for _ in range(rows + 1)]
    count = 0

    for i in range(1, rows + 1):
      for j in range(1, cols + 1):
        x = 1 if grid[i - 1][j - 1] == 'X' else 0
        y = 1 if grid[i - 1][j - 1] == 'Y' else 0
        x = x + p[i - 1][j][0] + p[i][j - 1][0] - p[i - 1][j - 1][0]
        y = y + p[i - 1][j][1] + p[i][j - 1][1] - p[i - 1][j - 1][1]

        if x > 0 and x == y:
          count += 1

        p[i][j] = (x, y)

    pprint(p)

    return count

solution = Solution()
# print(solution.numberOfSubmatrices([["X","Y","."],["Y",".","."]]))
print(solution.numberOfSubmatrices([[".","."],[".","."]]))
#           0 0 0 0
# 1 0 1.    0 1 1 2
# 1 1 0.    0 2 3 4
