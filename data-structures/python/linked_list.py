class Node:
  def __init__(self, val, next = None):
    self.val = val
    self.next = next

  def __str__(self) -> str:
    return str(self.val)

def run_after(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)  # Run the actual method
        self._after_each()                    # Run your "end code"
        return result                         # Return the original result
    return wrapper

class LinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
    self.size = 0

  @property
  def is_empty(self):
    return self.head is None

  def _after_each(self):
    print("i love you")

  @run_after
  def append(self, val):
    node = Node(val)

    if self.tail is None:
      self.head = node
      self.tail = node

    else:
      self.tail.next = node
      self.tail = node
    self.size += 1

  def display(self):
    elements = ""

    curr = self.head
    while curr is not None:
      elements += str(curr) if not elements else " -> " + str(curr)
      curr = curr.next

    return elements

  def __str__(self) -> str:
    return self.display() + " { size: " + str(self.size) + " }"

  def __len__(self):
    return self.size

  def prepend(self, val):
    node = Node(val, self.head)
    self.head = node
    self.size += 1

  def insert(self, val, index):
    if index > len(self):
      raise IndexError("index beyond bounds")

    i = 0
    curr = self.head
    node = Node(val)

    if index == 0:
      self.prepend(val)
      return

    if index == len(self):
      self.append(val)
      return

    while i < index:
      if curr is None:
        curr = Node(None)

      if i == index - 1:
        node.next = curr.next
        curr.next = node
        self.size += 1
        return

      curr = curr.next
      i += 1

  def pop(self):
    curr = self.head

    while True:
      if curr is None:
        return None
      if curr.next is self.tail:
        tail = self.tail
        curr.next = None
        self.tail = curr
        self.size -= 1
        return tail

      curr = curr.next

  def pop_left(self):
    if self.head is None:
      return None
    val = self.head.val
    self.size -= 1
    self.head = self.head.next
    return val

  def remove(self, val):
    curr = self.head

    if curr is None:
      return None

    if curr.val == val:
      return self.pop_left()

    while curr is not None:
      if curr.next is not None and  curr.next.val == val:
        curr.next = curr.next.next

        return val




list = LinkedList()
list.append(4)
list.append(9)
list.prepend(78)
list.append(13)
list.prepend(3)
# print(list)
# print(list.size)
list.insert(20, list.size)

print(list)
print(list.pop())
print(list)

print(list.pop_left())
print(list)

print(list.remove(78))
print(list)
