# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 내 풀이
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val > val:
                if root.left:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        else:
            root = TreeNode(val)
        return root
