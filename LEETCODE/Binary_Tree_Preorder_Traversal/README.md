# [LEETCODE] Binary Tree Preorder Traversal

배열로 주어진 이진 트리를 PreOrder - Traversal, 전위순회 하기. (재귀 & 순회)

### 재귀 & 순회

재귀적 방법과 순회하는 방법이 있다.

재귀적 방법은 노드 방문시 루트 값을 넣고 왼쪽, 오른쪽을 재귀적으로 방문한다.

순회하는 방법은 stack을 사용해 node가 있으면 값을 결과에 넣고, 오른쪽, 왼쪽 순으로 스택에 넣는다. 이렇게 하면 왼쪽 먼저 꺼내진다.
