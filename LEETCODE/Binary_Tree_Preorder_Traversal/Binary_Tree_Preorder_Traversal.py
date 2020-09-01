# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def __init__(self):
        self.nodes = []

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.nodes.append(root.val)
            if root.left:
                self.preorderTraversal(root.left)
            if root.right:
                self.preorderTraversal(root.right)

        return self.nodes

    # iterative
    def preorderTraversalWithIterative(self, root: TreeNode) -> List[int]:
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                stack.append(node.right)  # 오른쪽
                stack.append(node.left)  # 왼쪽 넣기

        return result
