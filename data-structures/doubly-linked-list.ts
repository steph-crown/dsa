class NodeItem<T> {
  data: T;
  next: NodeItem<T> | null;
  prev: NodeItem<T> | null;

  constructor(data: T, prev: NodeItem<T> | null, next: NodeItem<T> | null) {
    this.data = data;
    this.next = next;
    this.prev = prev;
  }

  public setNext(next: NodeItem<T> | null) {
    this.next = next;
    return this;
  }

  public setPrev(prev: NodeItem<T> | null) {
    this.prev = prev;
  }

  public setData(data: T) {
    this.data = data;
    return this;
  }

  toString(): string {
    return this.data?.toString() || "";
  }
}

export class DoublyLinkedList<T> {
  private head: NodeItem<T | null> | null = null;
  private tail: NodeItem<T | null> | null = null;
  size = 0;

  constructor() {}

  public isEmpty() {
    return this.size === 0;
  }

  // complexity: O(1)
  public append(data: T) {
    const node = new NodeItem(data, this.tail, null);

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
      const node = new NodeItem(data, null, null);
      this.head = this.tail = node;
    } else {
      const node = new NodeItem(data, null, this.head);
      this.head = node;
    }

    this.size++;
  }

  // get the first value if it exists
  // O(1)
  public peekFirst() {
    if (this.isEmpty()) throw new Error("No data");
    return this.head?.data;
  }

  // get the last value if it exists
  // O(1)
  public peekLast() {
    if (this.isEmpty()) throw new Error("No data");
    return this.tail?.data;
  }

  public removeFirst() {
    if (this.isEmpty()) throw new Error("No data");
    const next = this.head?.next;
    const data = this.head?.data;

    if (!next) {
      this.head = this.tail = null;
      this.size = 0;
    } else {
      this.head = next;
      this.head.prev = null;
      --this.size;
    }

    return data;
  }

  // remove last item
  // O(n)
  public removeLast() {
    if (this.isEmpty()) throw new Error("No data");

    const data = this.tail?.data;

    if (this.tail) {
      this.tail = this.tail?.prev;
      this.tail!.next = null;
      --this.size;

      if (this.isEmpty()) {
        this.head = null;
      }
    }

    return data;
  }

  public remove(node: NodeItem<T>) {
    if (!node.next) {
      this.removeLast();
    }

    if (!node.prev) {
      this.removeFirst();
    }

    node.prev!.next = node.next;
    node.next!.prev = node.prev;

    const data = node.data;

    node.prev = node.next = null;

    return data;
  }

  // clear
  // complexity: O(n)
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

// const list = new DoublyLinkedList();
// list.append(8);
// list.append(4);
// list.prepend(1);
// list.removeFirst();
// console.log({ thelist: list });
// list.removeLast();
// console.log({ thelist: list });
