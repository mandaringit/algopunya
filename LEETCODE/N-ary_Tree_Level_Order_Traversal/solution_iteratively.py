"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        level = {}

        q = deque()
        q.append((root, 1))

        while q:
            node, depth = q.popleft()

            if node:
                if depth in level:
                    level[depth].append(node.val)
                else:
                    level[depth] = [node.val]

                for child in node.children:
                    q.append((child, depth + 1))

        return [level[key] for key in level.keys()]
