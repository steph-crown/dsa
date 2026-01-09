class INode<T> {
  left: INode<T> | null;
  val: T;
  right: INode<T> | null;

  constructor(val: T) {
    this.left = null;
    this.val = val;
    this.right = null;
  }
}

class BinaryTree<T> {
  root: INode<T> | null;

  constructor() {
    this.root = null;
  }

  insert(val: T) {
    const node = new INode(val);

    if (!this.root) {
      this.root = node;
      return;
    }

    const queue: INode<T>[] = [this.root];

    while (queue.length) {
      const currentNode = queue.shift()!;

      if (!currentNode.left) {
        currentNode.left = node;
        return;
      } else {
        queue.push(currentNode.left);
      }

      if (!currentNode.right) {
        currentNode.right = node;
        return;
      } else {
        queue.push(currentNode.right);
      }
    }
  }

  from(arr: T[]) {
    for (let item of arr) {
      this.insert(item);
    }
  }
}

const tree = new BinaryTree();
tree.from([2, 3, 4, 4, 5]);

console.log({ tree });
