# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:

        stack = [(root, 0)]
        total = 0

        while stack:
            node, prev = stack.pop()
            if node:
                now = node.val if prev == 0 else (prev << 1) | node.val

                if not node.left and not node.right:
                    total += now
                else:
                    stack.append((node.left, now))
                    stack.append((node.right, now))

        return total
