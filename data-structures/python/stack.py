from collections import deque
from pprint import pprint

# stack = deque()
# stack.append(34)
# stack.append(22)
# stack.pop()

# arr = []
# arr.append(23)
# arr.append(34)
# arr.pop()
# print(arr)
# pprint(dir(stack))

# "we will conquer"
def reverse_str(s: str) -> str:
  stack = deque()
  res = []

  for char in s:
    stack.append(char)

  while len(stack):
    res.append(stack.pop())

  return "".join(res)

pprint(reverse_str("we will conquer"))
