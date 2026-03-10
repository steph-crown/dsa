class Solution:
    def isPalindrome(self, s: str) -> bool:
      s = s.lower()
      # two converging pointers l and r
      # while l < r
        # if l and r are alphanumeric, check if the same. if yes l++, r--, then continue, else return false
        # if l is not alphanumeric, l++
        # if r isnt alphanumeric, r--
      # return true
      l, r = 0, len(s) - 1

      while l < r:
        if s[l].isalnum() and s[r].isalnum():
          if s[l] == s[r]:
            l += 1
            r -= 1
            continue
          else:
            return False
        if not(s[l].isalnum()):
          l += 1
        if not(s[r].isalnum()):
          r -= 1
      return True

solution: Solution = Solution()
print(solution.isPalindrome("race a car"))
