// FIFO

import { DoublyLinkedList } from "./doubly-linked-list";

// insert element through the back and remove from the front.
class Queue<T> {
  list = new DoublyLinkedList();

  enqueue(value: T) {
    this.list.append(value);
    // console.log({ inro: this.list });
  }

  dequeue() {
    this.list.removeFirst();
  }

  toString() {
    return this.list.toString();
  }

  get size() {
    return this.list.size;
  }

  get isEmpty() {
    return this.size === 0;
  }

  peek() {
    if (this.isEmpty) {
      throw new Error("Empty queue");
    }

    return this.list.peekFirst();
  }
}

const queue = new Queue();
queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.dequeue();
queue.enqueue(4);
queue.enqueue(5);

console.log({ string: queue.toString(), size: queue.size });
