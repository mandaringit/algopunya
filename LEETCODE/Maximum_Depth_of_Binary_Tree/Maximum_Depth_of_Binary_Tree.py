# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        if root:
            stack = [(root, 1)]
            while stack:
                node, depth = stack.pop()
                if node:
                    max_depth = max(max_depth, depth)
                    stack.append((node.right, depth + 1))
                    stack.append((node.left, depth + 1))

        return max_depth

    # recursive
    def maxDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
