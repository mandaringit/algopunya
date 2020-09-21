"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result = []

        def traverse(root):
            if root:
                result.append(root.val)
                for child in root.children:
                    traverse(child)

        traverse(root)
        return result
