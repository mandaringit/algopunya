# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = even_head = head.next
        # even의 next.next를 보장하기 위한 조건
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            even.next = even.next.next
            even = even.next

        # 잇기
        odd.next = even_head
        return head
