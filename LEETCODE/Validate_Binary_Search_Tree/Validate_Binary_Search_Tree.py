# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # iterative
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    length = len(result)
                    if length == 0:
                        result.append(node.val)
                    elif length > 0 and node.val > result[length - 1]:
                        result.append(node.val)
                    else:
                        return False
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return True

    # recursive
    def isValidBST2(self, root: TreeNode, floor=float('-inf'), celing=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= celing:
            return False

        return self.isValidBST(root.left, floor=floor, celing=root.val) and self.isValidBST(root.right, floor=root.val, celing=celing)
