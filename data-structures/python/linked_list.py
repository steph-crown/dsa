class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __str__(self) -> str:
    return str(self.val)

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  @property
  def is_empty(self):
    return self.head is None

  def append(self, val):
    node = Node(val)

    if self.tail is None:
      self.head = node
      self.tail = node

    else:
      self.tail.next = node
      self.tail = node

  def display(self):
    elements = ""

    curr = self.head
    while curr is not None:
      elements += str(curr) if not elements else " -> " + str(curr)
      curr = curr.next

    return elements

  def prepend(self, val):
    node = Node(val, self.head)
    self.head = node



list = LinkedList()
list.append(4)
list.append(9)
list.prepend(78)
list.append(13)
list.prepend(3)
print(list.display())
