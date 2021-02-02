# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 값만 바꾸기
    def swapPairs(self, head: ListNode) -> ListNode:

        root = head

        while head and head.next:
            head.val, head.next.val = head.next.val, head.val
            head = head.next.next

        return root

    # 노드 바꾸기 (iterative)
    def swapPairs(self, head: ListNode) -> ListNode:

        root = prev = ListNode(None)
        # head & head.next가 없는 경우엔 head 그대로리턴하기 위함
        prev.next = head

        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    # 노드 바꾸기 (recursive)
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head
