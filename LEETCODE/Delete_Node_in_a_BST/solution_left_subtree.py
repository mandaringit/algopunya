# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:  # 발견시 행동

            if not root.right:  # 오른쪽 자식이 없으면
                return root.left  # 이제 루트는 왼쪽 루트로 교체됨

            if not root.left:  # 왼쪽 자식이 없으면
                return root.right  # 루트는 오른쪽 루트로 교체됨

            # 둘다 있다면 우리는 왼쪽 서브트리 중 가장 큰 값을 찾아 교체하러간다.
            temp = root.left
            bigger = temp.val
            while temp.right:
                temp = temp.right
                bigger = temp.val
            # 지금 루트값을 교체한다
            root.val = bigger

            # 그 다음 왼쪽 서브트리의 가장 큰 값을 지운다.
            root.left = self.deleteNode(root.left, root.val)
        return root
