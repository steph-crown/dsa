from typing import Optional, Tuple

def log(func):
  def wrapper(self, *args, **kwargs):
    print(f"args: {args}: \n CACHE: {self}\n\n")
    result = func(self, *args, **kwargs)
    return result
  return wrapper

class Node:
  def __init__(self, key: int, val: int) -> None:
    self.key, self.val = key, val
    self.prev: Optional["Node"] = None
    self.next: Optional["Node"] = None

class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}
    self.left = self.right = None

  def __str__(self) -> str:
    curr = self.left
    res = []
    while curr:
      res.append(f"({curr.key}, {curr.val})")
      curr = curr.next
    return " <-> ".join(res)

  @log
  def get(self, key: int) -> int:
    # get from cache
    # if exists set the node as right MRU retuirn val
    # else return -1
    node = self.cache.get(key)
    if node:
      self._move_right(node)
      return node.val
    return -1

  def _move_right(self, node: Node):
    if not node or node is self.right:
      return
    if node is self.left and self.left:
      self.left = self.left.next
    prev = node.prev
    nxt = node.next
    if prev:
      prev.next = nxt
    if nxt:
      nxt.prev = prev
    if self.right:
      self.right.next = node
    node.prev = self.right
    node.next = None
    self.right = node

  def _set_right(self, key: int, val: int):
    node = Node(key, val)
    if not self.left and not self.right:
      self.left = self.right = node
    else:
      if self.right:
        self.right.next = node
      node.prev = self.right
      self.right = node
    return node

  def remove_left(self):
    left = self.left
    if not left:
      return
    if left is self.right:
      self.left = self.right = None
    nxt = left.next
    if nxt:
      nxt.prev = None
    self.left = nxt
    del self.cache[left.key]

  @log
  def put(self, key: int, val: int) -> None:
    # if key is in, get node
    # update val in node, then move to the right
    # if key not in node,
    # if less than capacity, create node, set as the right node, and add to cache
    # if at capacity, remove left, and do previous step
    node = self.cache.get(key)
    if node:
      node.val = val
      self._move_right(node)
      return
    if self.size == self.capacity:
      self.remove_left()
    node = self._set_right(key, val)
    self.cache[key] = node

  @property
  def size(self) -> int:
    return len(self.cache)

cache = LRUCache(3)



"""
use doubly linked list and map
map stores key and value will be node in the list
put(...)
  1. if key not in map, append to list, put in map with list node
  2. if key in map, get the node value, remove from list and append, update the value
  3. if size was at capacity and key not in map, shift (remove first) in list, get the key from there and rmeove in map as well.
get(...)
  1. if key in map, get node value, shift and append
  2. if not in map, return -1
"""
