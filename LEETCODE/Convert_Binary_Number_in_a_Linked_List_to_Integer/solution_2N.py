# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        values = []

        while head:
            values.append(head.val)
            head = head.next

        multiplier = 0
        total = 0
        for i in range(len(values)-1, -1, -1):

            total += values[i] * (2 ** multiplier)
            multiplier += 1

        return total
