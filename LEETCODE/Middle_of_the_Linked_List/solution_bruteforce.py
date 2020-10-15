# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        nodes = []

        while head:
            nodes.append(head)
            head = head.next

        mid = len(nodes) // 2

        return nodes[mid]
