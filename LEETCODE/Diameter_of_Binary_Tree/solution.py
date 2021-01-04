# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self) -> None:
        self.ans = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 왼쪽 제일 끝 + 오른쪽 제일 끝 이아니다!!
        def depth(node):
            if not node:
                return 0

            # 현재 노드의 왼쪽, 오른쪽 자식의 깊이를 구한다.
            left = depth(node.left)
            right = depth(node.right)

            # 지금까지 구한 최대 지름 vs 현재 노드의 지름
            self.ans = max(self.ans, left + right)

            # 노드의 왼쪽 또는 오른쪽 중 "가장 긴쪽의 길이"만이 필요함
            return 1 + max(left, right)

        depth(root)

        return self.ans
