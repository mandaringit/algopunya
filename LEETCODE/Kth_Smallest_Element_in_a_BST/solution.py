# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = []
        stack = []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            node = stack.pop()
            if len(result) == k-1:
                return node.val
            result.append(node.val);
            
            root = node.right