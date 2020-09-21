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
        stack = [root]

        while stack:
            node = stack.pop()

            if node:
                result.append(node.val)
                for child in node.children:
                    stack.append(child)

        return result[::-1]
