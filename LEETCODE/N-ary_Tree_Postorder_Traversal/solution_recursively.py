"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result = []

        def helper(root):
            if root:
                for child in root.children:
                    helper(child)
                result.append(root.val)

        helper(root)

        return result
