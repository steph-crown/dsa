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
  private head: NodeItem<T | null> | null = null;
  private tail: NodeItem<T | null> | null = null;
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

    this.size++;
  }

  // insert value after another value
  // complexity: O(N)
  public insertAfter(data: T, newValue: T) {
    let trav = this.head;

    while (trav) {
      if (!trav) {
        throw new Error("No data found");
      }

      if (trav.data === data) {
        const node = new NodeItem(newValue, trav.next);

        if (!trav.next) {
          this.tail = node;
        }

        trav.next = node;

        this.size++;
        return node;
      }

      trav = trav?.next;
    }
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

    if (!next) {
      this.head = this.tail = null;
      this.size = 0;
    } else {
      this.head = next;
      --this.size;
    }
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

const list = new SinglyLinkedList();
list.append(8);
list.append(4);
list.prepend(1);
list.insertAfter(4, 5);
list.removeFirst();
console.log({ thelist: list, first: list.peekFirst(), last: list.peekLast() });
