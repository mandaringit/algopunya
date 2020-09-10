# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head and head.next:
            # A - 기존 head, B - head.next, C - head.next.next
            temp = head.next  # B는 일단 킵해두고

            # C가 있으면 나랑 같은 작업을 하게 하고 그렇게 바뀐 C를
            # B랑 교체한다.
            head.next = self.swapPairs(temp.next)

            # B의 옆을 A로 바꾼다
            temp.next = head

            return temp  # B가 가장 앞서므로 B를 돌려준다.
        return head
