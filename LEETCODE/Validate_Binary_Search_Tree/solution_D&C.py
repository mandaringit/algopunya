# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive
    def isValidBST(self, root: TreeNode, floor=float('-inf'), celing=float('inf')) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= celing:
            return False

        return self.isValidBST(root.left, floor=floor, celing=root.val) and self.isValidBST(root.right, floor=root.val, celing=celing)
