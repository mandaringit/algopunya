# Definition for singly-linked list.
from collections import deque


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 리스트로 변환 후 팰린드롬 판별
    def isPalindrome(self, head: ListNode) -> bool:
        q: list = []

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True

    # 팰린드롬 판별을 deque으로 최적화
    def isPalindrome(self, head: ListNode) -> bool:
        q = deque()

        if not head:
            return True

        node = head

        while node:
            q.append(node.val)
            node = node.next

        while len(q) > 1:
            if q.popleft() != q.pop():
                return False

        return True

    # Runner 풀이
    def isPalindrome(self, head: ListNode) -> bool:

        if not head:
            return True

        rev = None  # 역순 만들기 용
        slow = fast = head

        # 중간을 찾아가는 동시에, slow를 이용해 그 반쪽을 역순으로 바꾼다.
        while fast and fast.next:
            fast = fast.next.next
            # 다중 처리 중요. 나눠서 처리하면 결과가 다르다.
            rev, rev.next, slow = slow, rev, slow.next

        # 갯수가 홀수일때 처리
        if fast:
            slow = slow.next

        # 역순으로 가면서 비교
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
