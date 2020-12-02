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

function traverse(node: TreeNode | null, result: number[]): void {
  if (!node) return;

  traverse(node.left, result);
  result.push(node.val);
  traverse(node.right, result);
}

function inorderTraversal(root: TreeNode | null): number[] {
  const result = [];
  traverse(root, result);

  return result;
}

function inorderTraversalIteravel(root: TreeNode | null): number[] {
  if (!root) return [];

  const result = [];
  const stack = [];

  while (true) {
    while (root) {
      stack.push(root);
      root = root.left;
    }

    if (stack.length === 0) break;

    const node = stack.pop();
    result.push(node.val);

    root = node.right;
  }

  return result;
}
