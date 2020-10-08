# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:

        if not t1 and not t2:
            return None

        merged = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
        merged.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
        merged.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)

        return merged
