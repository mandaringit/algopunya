# [LEETCODE] Binary Search Tree Iterator

이진 탐색 트리 BST 이터레이터를 직접 구현해보는 문제

- next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
- You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.

### 미리 순회해서 내림차순으로 모아놓기

next()를 호출하면 작은 숫자부터 차례대로 뽑아내고, hasNext()를 호출하면 다음 수가 있는지 확인해주면 된다. 접근 시간이 O(1)이기 때문에 미리 중위순회로 오름차순으로 뽑아낸 후 pop(), 길이를 이용해 각자를 구현하면 좋을것 같다는 생각으로 문제를 풀었다.

만약 오름차순으로 정렬한다면 앞에서부터 숫자를 빼야 next() 함수가 구현되는 것이기 때문에 pop(0)를 써야한다. 그러나 pop(0) 같은 경우 deque이 아니면 O(N)의 시간이 추가되므로 내림차순으로 모아놓으면 되겠다는 생각을 했다. 중위순회는 돌면 오름차순이지만 이걸 left, right 넣는 순서를 바꿔서 내림차순 정렬,하여 pop()을 사용했다.

처음 순회에 O(N)이 이미 지나버리니 이터레이터 의미와 조금 다르지 않나 싶긴 하다..

### 이터레이터의 의미에 더 맞는 풀이

내가 한꺼번에 모아서 해결했다면, 다른사람들은 어떻게 했을까.

일단 이분들은 시작과 함께 루트가 있으면, 왼쪽 서브트리만 모두 돌면서 스택에 집어 넣는다.

```py
def __init__(self, root):
    self.stack = []
    while root:
        self.stack.append(root)
        root = root.left
```

그리고 next()를 호출하면, stack에서 pop()한 노드를 가지고 오른쪽 서브트리를 확인후 작업한다.

```py
def next(self):
    # 1. 꺼낸 노드에 오른쪽 서브트리가 있으면 해당 노드의 왼쪽만 모두 다시 스택에 집어넣는다.
    node = self.stack.pop()
    x = node.right
    while x:
        self.stack.append(x)
        x = x.left
    #2. 꺼낸 노드의 값을 리턴한다.
    return node.val
```

이런식으로 구현했다. next() 호출 시에만 다음 노드를 찾아가는 모양으로, 이터레이터에 더 맞는 풀이라고 생각한다.
