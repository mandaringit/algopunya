# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # 리스트노드를 뒤집고 리스트로 만든 다음 더해서 다시 리스트노드로 만들기
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def reverseList(head):
            node, prev = head, None

            while node:
                next, node.next = node.next, prev
                prev, node = node, next
            return prev

        def toList(sll: ListNode) -> List:
            l = []
            while sll:
                l.append(sll.val)
                sll = sll.next

            return l

        def toReversedListNode(l: List) -> ListNode:
            prev = None
            for num in l:
                node = ListNode(val=num, next=prev)
                prev = node

            return prev

        original1 = int(''.join(map(str, toList(reverseList(l1)))))
        original2 = int(''.join(map(str, toList(reverseList(l2)))))

        return toReversedListNode(list(str(original1 + original2)))

    # 전가산기 개념? 올림수 하나를 관리하면서 진행하기.
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        result = result_head = ListNode(0)

        carry = 0  # 올림수
        while l1 or l2 or carry:
            summation = 0

            if l1:
                summation += l1.val
                l1 = l1.next

            if l2:
                summation += l2.val
                l2 = l2.next

            carry, value = divmod(carry + summation, 10)
            result.next = ListNode(value)
            result = result.next

        return result_head.next  # 초기 ListNode(0)을 지우기 위함
