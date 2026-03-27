from typing import List

class Solution:
  def areSimilar(self, mat: List[List[int]], k: int) -> bool:
    """
    loop through rows,
    for each row apply the logic to shift, and compare. if any difference return false, else proceed
    return true

    0, 1, 2, 3
    """
    rows, cols = len(mat), len(mat[0])

    for i in range(rows):
      for j in range(cols):
        new_pos = (j - k if i % 2 == 0 else j + k) % cols
        if mat[i][j] != mat[i][new_pos]:
          return False

    return True

solution = Solution()
print(solution.areSimilar([[1,2,1,2],[5,5,5,5],[6,3,6,3]], 2))
