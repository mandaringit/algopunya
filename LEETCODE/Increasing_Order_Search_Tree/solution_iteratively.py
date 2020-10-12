# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        tree = None
        next_tree = tree

        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    if not tree:
                        tree = TreeNode(node.val)
                        next_tree = tree
                    else:
                        next_tree.right = TreeNode(node.val)
                        next_tree = next_tree.right
                else:
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))

        return tree


"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root, tail = None):
        tree = None
        next_tree = tree
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return tree
            
            node = stack.pop()    
            if not tree:
                tree = TreeNode(node.val)
                next_tree = tree
            else:
                next_tree.right = TreeNode(node.val)
                next_tree = next_tree.right
            
            root = node.right
"""
