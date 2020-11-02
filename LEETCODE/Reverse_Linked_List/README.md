# [LEETCODE] Reverse Linked List

링크드 리스트 뒤집기

### 접근

연결을 거꾸로 뒤집으면 되는건데,

1. 이전값을 저장할 prev = None에서 시작.
2. 다음 노드인 head.next를 임시로 저장
3. head.next를 prev를 가리키도록 한다.
4. prev는 이제 next를 변경한 현재 head를 가리키도록 한다.
5. 임시로 저장한 head.next로 이동해 동일한 과정 반복.
