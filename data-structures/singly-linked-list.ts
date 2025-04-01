class NodeItem<T> {
  data: T;
  next: NodeItem<T> | null;

  constructor(data: T, next: NodeItem<T> | null) {
    this.data = data;
    this.next = next;
  }

  public setNext(next: NodeItem<T> | null) {
    this.next = next;
    return this;
  }

  public setData(data: T) {
    this.data = data;
    return this;
  }

  toString(): string {
    return this.data?.toString() || "";
  }
}

class SinglyLinkedList<T> {
  head: NodeItem<T | null> | null = null;
  tail: NodeItem<T | null> | null = null;
  size = 0;

  constructor() {}

  public isEmpty() {
    return this.size === 0;
  }

  // complexity: O(1)
  public append(data: T) {
    const node = new NodeItem(data, null);

    if (this.isEmpty()) {
      this.head = this.tail = node;
    } else {
      this.tail?.setNext(node);
      this.tail = node;
    }

    this.size++;
  }

  // complexity: O(1)
  public prepend(data: T) {
    if (this.isEmpty()) {
      const node = new NodeItem(data, null);
      this.head = this.tail = node;
    } else {
      const node = new NodeItem(data, this.head);
      this.head = node;
    }
  }

  public clear() {
    let trav = this.head;

    while (trav) {
      trav.data = null;
      const next = trav.next;

      trav.next = null;
      trav = next;
    }

    this.head = this.tail = null;
    this.size = 0;
  }
}

const list = new SinglyLinkedList();
list.append(8);
list.append(4);
list.append(9);
list.prepend(1);
console.log({ thelist: list });
list.clear();
console.log({ thelist: list });
