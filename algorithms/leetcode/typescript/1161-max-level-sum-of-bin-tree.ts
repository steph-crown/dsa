/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

type TreeNode = {
  val: number;
  left: TreeNode;
  right: TreeNode;
};

function maxLevelSum(root: TreeNode | null): number {
  let maxSum = -Infinity;
  let maxLevel = 0;

  if (!root) return 0;

  const queue = [root];

  let currLevel = 1;
  while (queue.length) {
    const queueLength = queue.length;
    let levelSum = 0;

    for (let i = 0; i < queueLength; i++) {
      const currentNode = queue.shift();
      if (!currentNode) continue;

      levelSum += currentNode.val;

      if (currentNode.left) queue.push(currentNode.left);
      if (currentNode.right) queue.push(currentNode.right);
    }

    if (levelSum > maxSum) {
      maxSum = levelSum;
      maxLevel = currLevel;
    }
    currLevel++;
  }

  return maxLevel;
}
