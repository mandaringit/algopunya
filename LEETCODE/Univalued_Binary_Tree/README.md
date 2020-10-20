# [LEETCODE] Univalued Binary Tree

이진트리의 모든 노드 값이 동일한지 체크

### 접근

이진트리를 모두 순회한다. 순회하면서 set으로 값을 수집하는데, 값이 두개 이상이면 False를 리턴한다. 순회하는 방법은 DFS나 BFS 또는 전위 중위 후위 순회 모두 상관없다.
