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

    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.nodes.append(root.val)

        return self.nodes

    # iterative
    def postorderTraversal2(self, root: TreeNode) -> List[int]:
        result = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))  # 가운데는 맨 마지막에
                    stack.append((node.right, False))  # 2번째로 오른쪽 방문
                    stack.append((node.left, False))  # 1번째로 왼쪽 방문

        return result
