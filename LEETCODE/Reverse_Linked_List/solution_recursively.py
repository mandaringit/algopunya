class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        self.reverse(head, None)

    def reverse(self, head, newHead):
        if not head:
            return newHead
        next = head.next
        head.next = newHead
        return self.reverse(head.next, head)
