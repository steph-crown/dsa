class PriorityQueue<T> {
  private heap: T[] = [];
  private map = new Map<T, Set<number>>();

  constructor();
  constructor(size: number);
  constructor(arr: T[]);

  constructor(sizeOrArr?: number | T[]) {
    if (typeof sizeOrArr === "number" || !sizeOrArr) {
      this.heap = new Array(sizeOrArr || 1);
    } else {
      this.heap = sizeOrArr;

      for (let i = 0; i < sizeOrArr.length; i++) {
        this.mapAdd(sizeOrArr[i], i);
      }

      for (let i = this.lastParent; i >= 0; i--) {
        this.sink(i);
      }
    }
  }

  get size() {
    return this.heap?.length || 0;
  }

  // if map has element, add to the set, else new entry
  private mapAdd(elem: T, i: number) {
    const existingSet = this.map.get(elem) || new Set();

    this.map.set(elem, existingSet.add(i));
  }

  isEmpty() {
    return this.size === 0;
  }

  clear() {
    this.map.clear();
    this.heap = [];
  }

  peek() {
    if (!this.heap?.length) return null;

    return this.heap[0];
  }

  poll() {
    return this.removeAt(0);
  }

  contains(elem: T) {
    if (!elem) return false;
    return this.map.has(elem);
  }

  add(elem: T) {
    if (!elem) throw new TypeError("Incorrect argument");
    this.mapAdd(elem, this.size);
    this.heap?.push(elem);

    this.swim(this.size - 1);
  }

  private getParent(idx: number) {
    return Math.floor((idx - 1) / 2);
  }

  // compare idx and parent.
  // while idx < parent and idx != 0, swap idx and parent.
  private swim(idx: number) {
    let parent = this.getParent(idx);

    while (idx !== 0 && !this.less(parent, idx)) {
      this.swap(idx, parent);

      idx = parent;
      parent = this.getParent(idx);
    }
  }

  private getLeftChild(idx: number) {
    return 2 * idx + 1;
  }

  private getRightChild(idx: number) {
    return 2 * idx + 2;
  }

  private getSmallestChild(idx: number) {
    let left = this.getLeftChild(idx);
    let right = this.getRightChild(idx);

    let smallest = left;

    if (this.less(right, left)) {
      smallest = right;
    }

    return smallest;
  }

  // check both children l, r
  // if not the same, swap idx with smaller
  // else swap with l
  // continue until idx >= l and idx >= r
  sink(idx: number) {
    while (true) {
      // let left = this.getLeftChild(idx);
      // let right = this.getRightChild(idx);

      // let smallest = left;

      // if (this.less(right, left)) {
      //   smallest = right;
      // }
      const smallest = this.getSmallestChild(idx);

      if (this.less(idx, smallest)) break;

      this.swap(idx, smallest);

      idx = smallest;
    }
  }

  private less(i: number, j: number) {
    if (!this.heap) return false;

    return this.heap[i] <= this.heap[j];
  }

  private swap(idx1: number, idx2: number) {
    const idx1El = this.heap[idx1];
    const idx2El = this.heap[idx2];

    this.heap[idx1] = idx2El;
    this.heap[idx2] = idx1El;

    this.mapSwap(idx1El, idx2El, idx1, idx2);
  }

  remove(elem: T) {
    const idx = this.mapGet(elem);

    if (idx) this.removeAt(idx);

    return false;
  }

  private mapSwap(idx1El: T, idx2El: T, idx1: number, idx2: number) {}

  removeAt(idx: number) {
    if (this.isEmpty()) {
      return null;
    }

    const idxEl = this.heap[idx];
    this.heap[idx] = this.heap.pop()!;

    const parent = this.getParent(idx);

    if (!this.less(parent, idx)) {
      this.swim(idx);
    } else if (!this.less(idx, this.getSmallestChild(idx))) {
      this.sink(idx);
    }

    this.mapRemove(idxEl, idx);
    return idxEl;
  }

  private get lastParent() {
    return Math.max(Math.floor(this.size / 2) - 1, 0);
  }

  private isNotParentChild(idx: number) {
    const lastParent = this.lastParent;
    if (idx > lastParent) return true;

    return false;
  }

  // if it is a leaf child, return true
  // if less than smallest child, return ismeanheap(leftchild) & ismeanheap(rightChild)
  // else return false
  isMinHeap(idx: number): boolean {
    if (this.isNotParentChild(idx)) return true;

    if (this.less(idx, this.getSmallestChild(idx))) {
      const left = this.getLeftChild(idx);
      const right = this.getRightChild(idx);
      return this.isMinHeap(left) && this.isMinHeap(right);
    }

    return false;
  }

  private mapRemove(el: T, idx: number) {
    const set = this.map.get(el);
    set?.delete(idx);

    if (set?.size === 0) {
      this.map.delete(el);
    }
  }

  private mapGet(el: T) {
    const set = this.map.get(el);

    if (!set) return null;

    return [...set][set.size - 1];
  }
}

const queue = new PriorityQueue([1, 10, 5, 4, 5, 6, 7, 8, 9, 10]);

queue.add(11);

console.log({ queue });
