from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def rev(self, l: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = l
    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
    return prev

  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    l1_rev = self.rev(l1)
    l2_rev = self.rev(l2)


    c = 0
    total = ListNode()

    while l1_rev or l2_rev or c:
      s = (l1_rev.val if l1_rev else 0) + (l2_rev.val if l2_rev else 0) + c
      c = s // 10
      node = ListNode(s % 10)
      print(f"totalbal: {total.val}")
      if total.val is not None:
        node.next = total
      total = node
      if l1_rev:
        l1_rev = l1_rev.next
      if l2_rev:
        l2_rev = l2_rev.next
    return total
