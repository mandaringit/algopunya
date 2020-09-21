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

        # (node, visited)
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()

            if node:
                if visited:
                    result.append(node.val)
                else:
                    stack.append((node, True))
                    for child in node.children[::-1]:
                        stack.append((child, False))

        return result
