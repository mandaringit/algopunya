# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        
        stack = [root]
        total = 0
        while stack:
            
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    total += node.val
                    stack.extend([node.left,node.right])
                elif node.val < L:
                    stack.append(node.right)
                elif node.val > R:
                    stack.append(node.left)
                    
        return total
                    