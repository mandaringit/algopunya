# [LEETCODE] Swap Node In Pairs

링크드 리스트가 주어졌을 때, 인접한 두개의 노드의 헤드를 서로 바꾸기.

### 재귀적 풀이

어렵진 않지만 순서가 약간 헷갈릴 수도있는데, 노드 3개가 있다고 생각하고 그림을 천천히 생각해보자. 근데 헷갈리는건 사실이다.ㅠㅠ

First, we swap the first two nodes in the list, i.e. head and head.next;
Then, we call the function self as swap(head.next.next) to swap the rest of the list following the first two nodes.
Finally, we attach the returned head of the sub-list in step (2) with the two nodes swapped in step (1) to form a new linked list.
