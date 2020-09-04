# [LEETCODE] Validate Binary Search Tree

이진 탐색 트리의 정의,

- The left subtree of a node contains only nodes with keys `less than` the node's key.
- The right subtree of a node contains only nodes with keys `greater than` the node's key.
- Both the left and right subtrees must also be binary search trees.

를 만족하는가?

### 중위순회 접근법

이진트리를 중위순회하면 오름차순 정렬된 배열을 얻게 된다고 했다. 그 점에 착안해 중위순회하면서 값을 넣을때마다 앞의 값을 비교해가며 값이 더 큰지 확인했다. 주의할 점은 여기선 크거나, 작거나이다. 같은 경우는 올바르지 않다고 봐야한다.

### 재귀적 접근법

다른 사람들은 재귀적으로 많이 풀었다. 내가 재귀적으로 생각했을때 어려웠던 점은 자기 자신만 확인하면 되는게 아니라 자신 이전의 노드값보다 작거나 크거나 하는 기준이 있기 때문에 그걸 어떻게 처리하나였는데, 여기선 밑으로 그걸 같이 전달해주면서 해결한거 같다.

여기서 floor와 celing은 이진 탐색 트리의 정의해 의한 각 노드가 가질 수 있는 최댓값과 최솟값의 범위라고 본다.

첫 노드는 -무한대 ~ 무한대까지 범위를 가질 수 있으므로 기본값을 이렇게 주었다고 생각된다.

그 다음 노드에서 조건 이진 탐색 트리의 조건을 확인하고 자신의 왼쪽, 오른쪽 노드로 내려간다.

왼쪽 노드의 (floor, celing) = (-무한대, 부모노드의 값)
오른쪽 노드의 (floor, celing) = (부모노드의 값, 무한대)

이렇게 재귀적으로 수행 가능하다.

```python
def isValidBST(self, root, floor=float('-inf'), ceiling=float('inf')):
    # 아무것도 없을땐 조건에 위배되는게 없으니 True
    if not root:
        return True
    # 노드 값이 작거나 같아버리거나,
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return self.isValidBST(root.left, floor, root.val) and self.isValidBST(root.right, root.val, ceiling)
```
