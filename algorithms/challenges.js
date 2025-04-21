// Project: HackerRank - Data Structures - Singly Linked Lists - Insert a node at the tail of a linked list, and returns the head of the modified linked list
function insertNodeAtTail(head, data) {
  const newNode = new SinglyLinkedListNode(data);

  // If the list is empty, return the new node as head
  if (!head) {
    return newNode;
  }

  // Traverse to the end of the list
  let current = head;
  while (current.next !== null) {
    current = current.next;
  }

  // Set the last node's next to point to the new node
  current.next = newNode;

  // Return the original head
  return head;
}
