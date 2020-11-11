# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        q = deque([(root.left, root.right)])

        while q:
            n1, n2 = q.popleft()

            if n1 and n2 and n1.val == n2.val:
                q.extend([(n1.left, n2.right), (n1.right, n2.left)])
            elif not n1 and not n2:
                continue
            else:
                return False

        return True
