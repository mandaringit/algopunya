from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        q = deque([[p, q]])

        while q:
            n1, n2 = q.popleft()
            if not n1 and not n2:
                continue
            elif n1 and not n2:
                return False
            elif not n1 and n2:
                return False
            else:
                if n1.val == n2.val:
                    q.append([n1.left, n2.left])
                    q.append([n1.right, n2.right])
                else:
                    return False

        return True
