class Solution:
    def reverseList(self, head):
        prev = None

        while head:
            curr = head  # 현재 노드 임시 저장
            head = head.next  # 다음 노드로 바꾸고
            curr.next = prev  # 현재 노드의 next 포인터를 이전 노드를 가리키도록 변경
            prev = curr  # 이전 노드를 현재로 변경

        # head가 None일때까지 가기 때문에 prev가 최종 head가 된다.
        return prev
