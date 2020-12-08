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

function kthSmallest(root: TreeNode | null, k: number): number {
  const stack = [];
  let kth = 1;

  while (true) {
    while (root) {
      stack.push(root);
      root = root.left;
    }

    const node = stack.pop();
    if (kth === k) return node.val;
    kth++;

    root = node.right;
  }
}
