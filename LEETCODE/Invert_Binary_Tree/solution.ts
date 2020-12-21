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

function invertTree(root: TreeNode | null): TreeNode | null {
  if (root) {
    const temp = root.left;
    root.left = invertTree(root.right);
    root.right = invertTree(temp);
  }

  return root;
}

// iterative
function invertTree2(root: TreeNode | null): TreeNode | null {
  if (!root) return root;
  const stack = [root];

  while (stack.length !== 0) {
    const node = stack.pop();
    const temp = node.left;
    node.left = node.right;
    node.right = temp;
    if (node.left) stack.push(node.left);
    if (node.right) stack.push(node.right);
  }

  return root;
}
