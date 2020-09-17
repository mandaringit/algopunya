# [LEETCODE] Same Tree

두 이진 트리가 주어질때, 같은지 확인하라.

### 접근

모두 순회하며 비교하는 방법밖에 없다.

> recursively

1. 양쪽 노드가 모두 없으면 둘은 동일함. = True 리턴
2. 어느 한쪽은 있고 한쪽은 없으면 둘은 다름. = False 리턴
3. 양쪽 노드가 모두 존재 & 값이 같으면 -> 양쪽의 left & right로 재귀 수행
4. 양쪽 노드가 모두 존재 & 값이 다르면 -> False 리턴

> iteratively

로직은 위와 동일하다. deque을 사용했고(리스트 + front/rear를 써도 상관 없다.) deque에 [q.left,p.left] 같은 형식으로 비교해야하는 대상 둘을 묶어서 넣어줬다.
