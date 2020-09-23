# [LEETCODE] Map Sum Pairs

독특한 insert와 sum 메서드를 가진 MapSum 클래스 완성하기.

### 접근

Trie를 활용해보았다. `insert`는 Trie의 insert 처럼 추가하고, `sum`은 해당 prefix가 나올때까지 노드를 타고 가다가 prefix가 나온 노드부터 그 자식 노드들을 모두 순회 (DFS & BFS) 하면서 val 값을 더해서 구하면 된다.
