# [LEETCODE] Sum of Root To Leaf Binary Numbers

모든 값이 0 또는 1인 이진 트리에서 가장 루트를 MSB로 해서, 리프노드까지 값으로 만들어지는 이진수의 합을 구하라.

### 접근

이진 트리를 순회(DFS & BFS)하고 마지막에 완성된 이진수의 값을 모두 더하면 된다.

이진수를 만드는 방법 중 바로 생각나는 방법은 배열에 각 값을 저장하면서 순회, 모두 모이면 reverse + join한 뒤 이를 `int('',2)`로 변경하는 방법이다.

엄청난 시간이 걸리진 않지만 변환하는 시간들이 좀 걸릴 것 같다.

두번째론 저번에 배웠던 방법인데, 이전 값을 왼쪽으로 쉬프팅하고 이번 노드의 값을 OR 연산으로 추가하는 방법이다. 즉 `(prev << 1) | node.val`하면 현재 노드의 값을 합친 이진수의 값을 구할 수 있다. 초기 값 설정을 위해 0인 경우 처리를 해주었다.

세번째 방법은 두번째와 같은데, 더블링이라는 방법으로 `prev * 2 + node.val`하여 구할 수 있다.

노드가 마지막인지 확인하는 방법은 left & right의 여부로 판단했다.
