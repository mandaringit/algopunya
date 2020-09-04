# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.result = []
        self.reverse_inorder(root)

    # 중위순회긴 한데 pop을 위해서 내림차순으로 정렬해야했다.
    # 그래서 오른쪽과 왼쪽 값을 반대로 넣어줬음.
    def reverse_inorder(self, root):
        if root:
            self.reverse_inorder(root.right)
            self.result.append(root.val)
            self.reverse_inorder(root.left)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        return self.result.pop()

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if len(self.result) > 0:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
