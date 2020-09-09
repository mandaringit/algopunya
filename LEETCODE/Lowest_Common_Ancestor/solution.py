# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        LCA = root
        while LCA:
            if LCA.val < p.val and LCA.val < q.val:
                LCA = LCA.right
            elif LCA.val > p.val and LCA.val > q.val:
                LCA = LCA.left
            else:
                return LCA
        return LCA
