# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 1 using helper & recursive
    def invertTree(self, root: TreeNode) -> TreeNode:

        def helper(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            helper(root.left)
            helper(root.right)

        helper(root)
        return root

    # 2 recursive !!
    def invertTree2(self, root: TreeNode) -> TreeNode:

        if root:
            root.left, root.right = self.invertTree(
                root.right), self.invertTree(root.left)

        return root
