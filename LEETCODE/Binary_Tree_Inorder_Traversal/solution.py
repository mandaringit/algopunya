# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traverse(node):
            if not node:
                return

            traverse(node.left)
            result.append(node.val)
            traverse(node.right)

        traverse(root)

        return result

    def inorderTraversalIteravel(self, root: TreeNode) -> List[int]:
        result = []
        stack = []

        while True:

            while root:
                stack.append(root)
                root = root.left

            if not stack:
                break

            node = stack.pop()
            result.append(node.val)

            root = node.right

        return result
