from typing import List

class Solution:
  def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
    """
    get prefix product
    get suffix product
    multiply both for each cell
    """
    rows, cols = len(grid), len(grid[0])

    # prefix product
    res = [([1] * cols) for _ in range(rows)]

    prefix_agg = 1
    suffix_agg = 1
    MOD = 12345

    for i in range(rows):
      for j in range(cols):
        m = rows - i - 1
        n = cols - j - 1

        res[i][j] = (prefix_agg * res[i][j]) % MOD
        prefix_agg = (prefix_agg * grid[i][j]) % MOD

        res[m][n] = (suffix_agg * res[m][n]) % MOD
        suffix_agg = (suffix_agg * grid[m][n]) % MOD

    return res

solution = Solution()
print(solution.constructProductMatrix([[12345],[2],[1]]))
