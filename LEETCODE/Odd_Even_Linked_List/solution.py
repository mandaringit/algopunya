# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # 노드가 2개 이상일때만 수행
        odd_start = head
        even_start = head.next

        odd = odd_start  # 0 ->
        even = even_start  # 1 ->
        head = head.next.next  # 2 ->

        while head:
            odd.next = head  # 0 -> 2
            even.next = head.next  # 1 -> 3
            # 다음 노드로 이동
            odd = odd.next
            even = even.next
            head = head.next.next if even else None  # 4

        # 홀수 노드 마지막 부분과 짝수 노드 시작부분을 이어준다.
        odd.next = even_start

        return odd_start
