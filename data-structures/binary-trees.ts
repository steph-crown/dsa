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

  depthFirst() {
    if (!this.root) return;

    const stack = [this.root];
    while (stack.length) {
      const currentNode = stack.pop();
      console.log(currentNode?.val);

      if (currentNode?.right) stack.push(currentNode.right);
      if (currentNode?.left) stack.push(currentNode.left);
    }
  }

  depthFirstRec(currentNode = this.root) {
    if (!currentNode) return;
    console.log(currentNode.val);

    if (currentNode.left) this.depthFirstRec(currentNode.left);
    if (currentNode.right) this.depthFirstRec(currentNode.right);
  }

  find(val: T) {
    if (!this.root) return false;

    const queue = [this.root];

    while (queue.length) {
      const currentNode = queue.shift();
      if (currentNode?.val === val) return true;

      if (currentNode?.left) queue.push(currentNode.left);
      if (currentNode?.right) queue.push(currentNode.right);
    }

    return false;
  }
}

const tree = new BinaryTree();
tree.from([2, 3, 4, 4, 5]);
// console.log();

console.log({ tree: tree.find(3) });

//       2
//    3     4
//  4  5
