# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        value = 0

        while head:
            value = value << 1 | head.val  # << shift + OR
            head = head.next

        return value
