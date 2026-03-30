from collections import Counter

class Solution:
  def checkStrings(self, s1: str, s2: str) -> bool:
    """
    create even and odd map for s1 chars
    loop through s2, and depending on position check the map to see if char is there
    """
    evens = Counter()
    odds = Counter()

    for (i, char) in enumerate(s1):
      if i % 2 == 0:
        evens[char] += 1
      else:
        odds[char] += 1

    for (i, char) in enumerate(s2):
      if i % 2 == 0:
        if evens[char] > 0:
          evens[char] -= 1
        else:
          return False
      else:
        if odds[char] > 0:
          odds[char] -= 1
        else:
          return False

    return True

solution = Solution()
print(solution.checkStrings("abcdba", "cabdab"))
print(solution.checkStrings("abe", "bea"))
