from typing import Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

  def append(self, val):
    node = ListNode(val)
    self.next = node
    return self

  def __str__(self) -> str:
    value = ""
    curr = self

    while curr is not None:
      value = f"{value} -> {self.val}"
      curr = curr.next
    return value

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    left = head
    right = head
    gap = -1

    while left and right:
      if gap == n:
        left = left.next
      else:
        gap += 1
      right = right.next
    print(f"left {left}")
