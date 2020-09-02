# [LEETCODE] Binary Tree Level Order Traversal

이진트리가 주어졌을때, Level Order - Traversal, 레벨 순회 하기

### 레벨순회

레벨 순회는 BFS로 순회하면 가능하다. 다만 깊이(레벨)를 알아야 하기 때문에 깊이와 함께 큐에 넣어줬다.

큐를 쓸때 q.pop(0)는 시간을 많이 잡아먹으므로 front/rear 인덱스를 사용해 써도 되고, deque을 사용해도 될것 같다.
