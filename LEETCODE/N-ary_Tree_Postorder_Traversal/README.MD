# N-ary Tree Postorder Traversal

N-ary Tree가 주어졌을 때, Postorder 하기

### 접근법

- recursively

  노드에 들어왔을때, 자식들을 먼저 재귀적으로 순회한 후, 자식이 없을때부터 노드 값을 저장한다.

- iteratively

  A. 방문여부를 파악하면서 진행하기. 노드 방문 시 자기 자신 포함, visited 플래그를 같이 저장해 스택에서 뽑힐 때 저장 여부를 판단하게 하는 방법이 있다. 뽑은 노드가 스택의 맨 처음에 들어가면 결과적으로는 가장 마지막에 뽑히게 된다.

  B. 다른 풀이들을 보니 postorder는 preorder를 오른쪽 서브트리로 순회한 다음 역으로 취하면 같은 결과를 얻을 수 있다는 사실!
