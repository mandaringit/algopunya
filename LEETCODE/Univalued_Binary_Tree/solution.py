# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        values = set()

        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                values.add(node.val)

                if len(values) >= 2:
                    return False

                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return True
