// Definition for a binary tree node.
class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function diameterOfBinaryTree(root: TreeNode | null): number {
  let answer = 0;

  return ((root: TreeNode | null): number => {
    const depth = (node: TreeNode | null) => {
      if (!node) return 0;

      const left = depth(node.left);
      const right = depth(node.right);

      answer = Math.max(left + right, answer);

      return 1 + Math.max(left, right);
    };

    depth(root);
    return answer;
  })(root);
}
