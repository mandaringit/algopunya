# [LEETCODE] Invert Binary Tree

이진트리 뒤집기 (대칭시키기)

### 접근

- recursive
  기본적인 생각은 노드에 도착했을 때, 좌 & 우를 서로 바꿔주면 뒤집는게 가능하다. 바로 밑에만 바꾸는게 아니라 재귀적으로 자식노드까지 바꿔줘야 한다.

  처음엔 helper함수를 만들어 좌,우를 서로 바꾼 뒤 각각에 대해 또 재귀적으로 수행했다. 또는 더 간단하게 바뀔 자식을 넣은 재귀함수를 바로 할당하며 수행하면 더 깔끔하게 표현이 가능해졌다.

- iterative
  스택 & 큐 로 DFS, BFS 둘중 아무거나 선택해서 풀면 된다. 결론은 모든 노드 방문해서 각 노드의 좌우 교환해주는 작업.