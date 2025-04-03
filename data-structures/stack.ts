import { DoublyLinkedList } from "./doubly-linked-list";

class Stack<T> {
  list = new DoublyLinkedList();

  constructor() {}

  push(data: T) {
    this.list.append(data);
  }

  pop() {
    if (this.isEmpty()) throw new Error("Stack is empty");
    return this.list.removeLast();
  }

  isEmpty() {
    return this.list.isEmpty();
  }

  peek() {
    return this.list.peekLast();
  }
}

const st = new Stack();
st.push(3);
st.push(3);
st.push(4);
console.log({ st, sss: st.pop() });
