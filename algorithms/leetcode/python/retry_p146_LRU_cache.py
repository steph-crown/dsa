from typing import Optional

def log(func):
  def wrapper(self, *args, **kwargs):
    print(f"args BEFORE: {args}: \n CACHE: {self}")
    result = func(self, *args, **kwargs)
    print(f"args AFTER: {args}: \n CACHE: {self}\n\n")
    return result
  return wrapper

class Node:
  def __init__(self, key: int, val: int) -> None:
    self.key = key
    self.val = val
    self.next: Optional["Node"] = None
    self.prev: Optional["Node"] = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.start, self.end = Node(0,0), Node(0,0)
    self.start.next = self.end
    self.end.prev = self.start

  def __str__(self) -> str:
    res = []
    curr = self.start
    while curr:
      res.append(str(curr.val))
      curr = curr.next
    return " <-> ".join(res)

  @property
  def size(self) -> int:
    return len(self.cache)



  @log
  def get(self, key: int) -> int:
    # is in map
      # yes, get node from cache, move to right and return value
      # no, return -1
    node = self.cache.get(key)
    if node:
      self._move_to_right(node)
      return node.val
    else:
      return - 1

  @log
  def put(self, key: int, val: int) -> None:
    # is in cache
      # yes, get node, update node val, move to right
      # no, create node, set to right, set in cache for key
    node = self.cache.get(key)
    if node:
      node.val = val
      self._move_to_right(node)
    else:
      if self.capacity == self.size:
        self._remove_first()
      node = Node(key, val)
      self._set_right(node)
      self.cache[key] = node

  def _move_to_right(self, node: Node):
    # if node.prev:
    #   node.prev.next = node.next
    # if node.next:
    #   node.next.prev = node.prev
    self._remove(node)
    self._set_right(node)
    self.cache[node.key] = node

  def _set_right(self, node: Node):
    if self.end.prev:
      self.end.prev.next = node
    node.prev = self.end.prev
    node.next = self.end
    self.end.prev = node

  def _remove_first(self):
    first = self.start.next
    if first:
      self._remove(first)
    # if first and first is not self.end:
    #   self.start.next = first.next
    #   if first.next:
    #     first.next.prev = self.start

  def _remove(self, node: Node):
    # if node.prev:
    node.prev.next = node.next
    if node.next:
      node.next.prev = node.prev
    del self.cache[node.key]
    # 0-3-4-0

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
