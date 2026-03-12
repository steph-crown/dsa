from collections import Counter

class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    """
    take every substing of length of s1 and compare with s1. if found return true, at end of loop return false

    define set, convert s1 to set
    i = 0 and
    while i < len(s2) - len(s1)
      for each item in window, check if in s1 set.
      if one is encountered not to be there, set i to the item after it
      if all is there return true
    at end return false
    """

    s1_counter = Counter(s1)
    s1_n = len(s1)
    s2_n = len(s2)

    i = 0
    for i in range(s2_n - s1_n + 1):
      check_counter = s1_counter.copy()
      for j in range(i, i + s1_n):
        is_last = (j == (i + s1_n - 1))
        if check_counter[s2[j]]:
          check_counter[s2[j]] -= 1
          if is_last:
            return True
        else:
          break

    return False

solution = Solution()
print(solution.checkInclusion("ab", "eidbjajbjaoo"))

        # print(f"check {check_counter}, s2j {s2[j]}, match {check_counter[s2[j]]}")
      # print(f"s1 {s1_counter}")
