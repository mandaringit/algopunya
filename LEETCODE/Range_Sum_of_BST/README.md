# [LEETCODE] Range Sum of BST

BST의 특정 구간 안에 포함된 수 모두 더하기

### 접근

1. Inorder 사용하기. BST에서 Inorder는 오름차순 정렬이 되므로 범위 내의 숫자까지만 찾아 더할 수 있다. 다만 거의 O(N)으로 볼 수 있을 것같다.

2. DFS & BFS를 활용해서, 범위에 따른 행동으로 탐색해간다. L <= val <= R 이면 값을 더하고 양쪽 자식 모두를 탐색, L보다 작으면 오른쪽만, R보다 크면 왼쪽만이 가능성이 있으므로 이들을 탐색한다. 비슷하게 O(N)일듯?
