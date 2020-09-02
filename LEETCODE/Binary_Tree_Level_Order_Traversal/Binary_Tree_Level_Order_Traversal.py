# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        q = [(root, 0)]
        front = 0
        rear = 1
        result = []
        while front != rear:
            node, level = q[front]
            front += 1

            if node:
                if len(result) == level:
                    result.append([node.val])
                else:
                    result[level].append(node.val)

                if node.left:
                    q.append((node.left, level + 1))
                    rear += 1

                if node.right:
                    q.append((node.right, level + 1))
                    rear += 1

        return result
