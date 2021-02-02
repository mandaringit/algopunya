# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        root = start = ListNode(None)  # 첫 시작점을 만들어준다.
        root.next = head  # 시작점 뒤에 head 이어주자 . root -> head

        # 뒤집어야 할 위치 이전까지 start 포인터를 이동시킨다.
        # 1->2->3->4->5 이고 m = 2 라면 start는 1까지만 이동한다.
        for _ in range(m - 1):
            start = start.next
        # 초기 end는 start의 바로 뒤에 위치시킨다. 여기선 2를 가리킨다.
        end = start.next

        # root(None) -> 1(start) ->  2(end) ->  3  ->  4  ->  5
        for _ in range(n - m):
            temp = start.next
            start.next, end.next = end.next, end.next.next
            start.next.next = temp
            # temp는 항상 start 바로 다음을 가리키는 포인터.
            # 뒤집기
            # 1 (start) -> 2 (temp)(end) -> 3 -> 4 -> 5
            # 1 (start) -> 3 (temp) -> 2(end) -> 4 -> 5
            # 1 (start) -> 4 (temp) -> 3 -> 2(end) -> 5

        return root.next
