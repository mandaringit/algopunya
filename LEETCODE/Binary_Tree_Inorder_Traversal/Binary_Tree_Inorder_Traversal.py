# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)

        return self.result

    # Iterative
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        result = []
        stack = []
        while True:
            # 왼쪽을 계속 집어넣으면서 가자
            while root:
                stack.append(root)
                root = root.left
            # 더이상 아무것도 없다면
            if not stack:
                return result

            # 왼쪽으로 들어가는게 끝이면
            node = stack.pop()  # 하나 꺼내서
            result.append(node.val)  # 값 저장
            root = node.right

    # Iterative 2 -- using flag
    def inorderTraversal2(self, root: TreeNode) -> List[int]:
        result = []
        stack = [(root, False)]

        while stack:
            node, visitied = stack.pop()
            if node:
                if visitied:
                    result.append(node.val)
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return result


sol = Solution()
sol.inorderTraversal2()
