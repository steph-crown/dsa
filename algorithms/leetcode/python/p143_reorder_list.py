from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    """
    get middle
    reverse second half (from middle)
    merge second half into first halff
    """

    # get middle
    slow, fast = head, head
    while slow and fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # reverse second half
    prev, curr = None, slow
    while curr:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    # merge
    first, second = head, prev
    while first and second and second.next:
      tmp1, tmp2 = first.next, second.next
      first.next = second
      second.next = tmp1
      second = tmp2
      first = tmp1


# 1-2-3-4-5
# 1-2-|5-4-3
