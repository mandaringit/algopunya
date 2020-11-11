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

function compare(left: TreeNode | null, right: TreeNode | null): boolean {
  if (left && right) {
    if (left.val === right.val) {
      const outer = compare(left.left, right.right);
      const inner = compare(left.right, right.left);
      return outer && inner;
    }
    return false;
  } else if (!left && !right) {
    return true;
  }
  return false;
}

function isSymmetric(root: TreeNode | null): boolean {
  if (!root) return true;
  return compare(root.left, root.right);
}
