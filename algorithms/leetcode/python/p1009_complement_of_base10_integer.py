class Solution:
  def bitwiseComplement(self, n: int) -> int:
    s = 0
    idx = 0

    if n == 0:
      return 1

    while n > 0:
      n, r = divmod(n, 2)
      s += (2 ** idx) if r == 0 else 0
      idx += 1

    return s

solution: Solution = Solution()
print(solution.bitwiseComplement(10))
