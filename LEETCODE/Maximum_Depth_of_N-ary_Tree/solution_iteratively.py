"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 0
        stack = [(root,1)]
        
        while stack:
            node, depth = stack.pop()
            
            if node:
                max_depth = max(max_depth, depth)
                
                for child in node.children:
                    stack.append((child,depth+1))
        
        return max_depth