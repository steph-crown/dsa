// Project: HackerRank - Data Structures - Linked Lists - Insert a node at the tail of a linked list, and returns the head of the modified linked list
function insertNodeAtTail(head, data) {
  const node = new SinglyLinkedListNode(data);

  let trav = head;
  let travNext = head?.next;

  if (!trav) {
    return node;
  }

  while (travNext) {
    // tail
    if (!travNext.next) {
      trav.next = node;
      travNext = null;
    } else {
      trav = travNext;
      travNext = travNext.next;
    }
  }

  return head;
}
