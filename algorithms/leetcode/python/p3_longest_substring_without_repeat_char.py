class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    """
    mark left to 0
    init longest = 0
    initialize set s with left in,
    for right from 1 to len(s)
      is right in set?
        yes,
          (set longest = max(longest, r - l))
          while l < r:
            remove l from set s
            l += 1
            is right in set?
              yes? continue inner loop
              no? add to set and break out of inner loop.
        no, add to set

        bacabcbb
    """

    if not s:
      return 0

    left, longest = 0, 1
    char_set = { s[0] }

    for right in range(1, len(s)):
      if s[right] in char_set:
        while left < right:
          char_set.remove(s[left])
          left += 1

          if s[right] not in char_set:
            char_set.add(s[right])
            break
      else:
        char_set.add(s[right])
        longest = max(longest, right + 1 - left)

    return longest

solution = Solution()
print(solution.lengthOfLongestSubstring(" "))
