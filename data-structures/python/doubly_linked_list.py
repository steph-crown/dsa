class Node:
  def __init__(self, val, prev = None, next = None) -> None:
    self.val = val
    self.prev = prev
    self.next = next

  def __str__(self) -> str:
    return str(self.val)

class DoublyLinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.size = 0

  @property
  def is_empty(self):
    return self.head is not None

  def append(self, val):
    node = Node(val)
    if self.tail is None:
      self.head = node
      self.tail = node
    else:
      self.tail.next = node
      node.prev = self.tail
      self.tail = node
    self.size += 1

  def display(self):
    curr = self.head
    if curr is not None:
      res = f"{curr.val}"
      curr = curr.next
    while curr is not None:
      res = f"{res} <-> {curr.val}"
      curr = curr.next
    return res

  def prepend(self, val):
    node = Node(val, None, self.head)
    if self.head is not None:
      self.head.prev = node
    self.head = node
    self.size += 1

  def __len__(self):
    return self.size

  def __str__(self) -> str:
    return f"{self.display()} \t size: {self.size} \t tail: {self.tail}"


list = DoublyLinkedList()
list.append(3)
list.append(9)
list.append(2)
list.append(4)
list.prepend(49)
print(list)
