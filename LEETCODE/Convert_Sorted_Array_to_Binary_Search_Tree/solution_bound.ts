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

function sortedArrayToBST(nums: number[]): TreeNode | null {
  function convert(left: number, right: number): TreeNode | null {
    if (left > right) {
      return null;
    }

    const mid = Math.floor((left + right) / 2);
    const node = new TreeNode(nums[mid]);

    node.left = convert(left, mid - 1);
    node.right = convert(mid + 1, right);

    return node;
  }

  return convert(0, nums.length - 1);
}
