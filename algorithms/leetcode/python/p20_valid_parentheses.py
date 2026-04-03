from collections import deque

class Solution:
  """
  for each, peek
  """
  def isValid(self, s: str) -> bool:
    stack = []
    matches = {")": "(", "}": "{", "]": "["}
    for char in s:
      if stack and matches.get(char) and stack[-1] == matches[char]:
        stack.pop()
      else:
        stack.append(char)
    return len(stack) == 0
