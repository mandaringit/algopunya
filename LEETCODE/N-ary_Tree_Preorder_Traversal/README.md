# N-ary Tree Preorder Traversal

n-ary 트리가 주어질 때, preorder 결과 반환하기

### 접근

- recursively

  노드를 뽑으면 바로 방문 & 자식 노드들 순서대로 순회(재귀적)

- iteratively

  스택을 사용한다. 노드 방문 시 결과에 저장하고, 자식의 순서를 거꾸로 스택에 넣으면 자식 노드 중 가장 처음 노드가 스택의 맨 뒤로 위치해 먼저 뽑힌다. 이렇게 preorder를 구현할 수 있다.
