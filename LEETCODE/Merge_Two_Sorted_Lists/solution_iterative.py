# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1 and not l2:
            return None
        elif not l2:
            return l1
        elif not l1:
            return l2

        root = None
        temp = root
        while l1 and l2:

            if l1.val < l2.val:
                node = ListNode(l1.val)
                l1 = l1.next
            else:
                node = ListNode(l2.val)
                l2 = l2.next

            if not root:
                root = node
                temp = node
            else:
                temp.next = node
                temp = temp.next

        if l1:
            temp.next = l1
        if l2:
            temp.next = l2

        return root
