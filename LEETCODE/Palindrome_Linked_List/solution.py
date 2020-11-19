# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # 절반 찾기
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # slow는 오른쪽 절반이 된다.
        # 뒤집는다.
        node = None
        while slow:
            curr = slow
            nxt = slow.next
            curr.next = node
            node = curr
            slow = nxt

        while head and node:
            if head.val != node.val:
                return False

            head = head.next
            node = node.next

        return True
