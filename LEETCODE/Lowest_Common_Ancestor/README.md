# [LEETCODE] Lowest Common Ancestor of a Binary Search Tree

이진 탐색 트리 BST에서 노드 두개가 주어지면 두 노드가 가지는 가장 낮은 공통 조상(Lowest Common Ancestor)을 찾아라.

### 접근

일단 특정 노드의 조상들은 어떻게 구할까? 바로 BST의 검색방법을 떠올리면 쉬울 것 같다. 특정 노드를 루트부터 찾아나가는 과정에 들리는 노드들이 특정 노드의 조상들이 될 것이다.

그렇다면 공통 조상은 어떻게 구할까?

생각해보면 두 노드 모두 BST에서 같은 방향으로 검색(p,q < node.val 또는 p,q > node.val)된다면 둘은 같은 방향의 자식 노드를 타고 계속해서 내려갈 것이고, 같은 조상을 공유하게 된다.

만약 그렇지 않게 된다면, 둘은 서로 왼쪽, 오른쪽으로 갈라지게 되고 이후 조상은 무조건 공통이 될 수 없으므로 갈라지는 순간의 노드가 공통 조상이 된다. 어느 한쪽(p 또는 q)에 도달하게 되는 경우도 마찬가지이다.
