# [LEETCODE] Search in a Binary Search Tree

이진 탐색 트리에서 검색 연산 구현하기

### recursively

root가 없으면 없다고 하면 되고, 있다면 값을 비교해서 동일한 값이라면 그대로 리턴, 목표하는 값보다 작으면 오른쪽으로, 크면 왼쪽 서브트리로 가면서 찾는 행위를 재귀적으로 반복했다.

### iteratively

while 문으로 찾을때까지 재귀에서 한것처럼 반복해서 순회하면 된다.
