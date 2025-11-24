class NodeEl<T> {
  value: T;
  prev: NodeEl<T> | null;
  next: NodeEl<T> | null;

  constructor(value: T, prev: NodeEl<T> | null, next: NodeEl<T> | null) {
    this.value = value;
    this.prev = prev;
    this.next = next;
  }
}

// doubly linked.
class LinkedList<T> {
  head: NodeEl<T> | null = null;
  tail: NodeEl<T> | null = null;
  size = 0;

  append(value: T) {
    const node = new NodeEl(value, this.tail, null);

    if (!this.head) {
      this.head = node;
    } else if (!this.tail) {
      this.tail = node;
      this.tail.prev = this.head;
      this.head.next = this.tail;
    } else if (this.tail) {
      this.tail.next = node;
      this.tail = node;
    }

    this.size++;
  }

  removeLast() {
    if (this.isEmpty) return;

    if (!this.tail) {
      this.head = null;
    } else {
      this.tail = this.tail.prev;
      if (this.tail) this.tail.next = null;
    }

    this.size--;

    if (this.isEmpty) {
      this.head === null;
    }
  }

  get isEmpty() {
    return this.size === 0;
  }

  toString() {
    // console.log({ this: this });
    let trav = this.head;
    let str = "";

    while (trav) {
      str = `${str}${(trav.value || "")?.toString()}`;
      trav = trav.next;
    }

    return str;
  }
}

class Stack<T> {
  list = new LinkedList<T>();

  pop() {
    this.list.removeLast();
  }

  push(value: T) {
    this.list.append(value);
  }

  get isEmpty() {
    return this.list.isEmpty;
  }

  get lastItem() {
    return this.list.tail?.value || this.list.head?.value || null;
  }

  toString() {
    return this.list.toString();
  }
}

function matchingBrackets(s: string) {
  const stack = new Stack<string>();
  const matchMap: Record<string, string> = {
    ")": "(",
    "]": "[",
    "}": "{",
  };

  for (let i of s) {
    if (stack.isEmpty) {
      stack.push(i);

      continue;
    }

    const lastItem = stack.lastItem;

    if (matchMap[i] === lastItem) {
      stack.pop();
    } else {
      stack.push(i);
    }
  }

  return stack.isEmpty;
}

console.log(matchingBrackets("[{}[(])](({{}})())"));
