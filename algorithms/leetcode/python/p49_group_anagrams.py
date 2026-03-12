from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    """
    for each word, sort and let it be key in a map that maps string to array of the words.
    """
    group = {}
    for word in strs:
      sorted_str = "".join(sorted(word))
      group.setdefault(sorted_str, []).append(word)

    return list(group.values())

solution = Solution()
print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
