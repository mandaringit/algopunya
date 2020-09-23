# [LEETCODE] Search a 2D Matrix II

각 row 별, col 별로 오름차순 정렬된 2차원 배열에서 효율적으로 숫자 찾기

### iteratively

왼쪽 아래에서부터 시작한다. 어째서 왼쪽 아래부터일까?

`[0,0]` & `[M-1,N-1]` 부터 시작한다면 좌표 이동이 무조건적인 증가 & 감소밖에 알 수가 없다. 즉 현재 위치의 수가 작거나 크다면 어디로 이동해야할지 방향을 잡을수가 없다.

그리고 `[0,N-1]`부터 시작하는 방법도 있겠지만, 이차원 배열 내부의 요소의 길이를 구해야 하기 때문에 다소 귀찮아질 수가 있다. -> `[]` 같은 입력이 주어진경우.

그러나 `[M-1, 0]`부터 시작한다면 이런 문제들로부터 좀 더 자유롭게 시작할 수 있다.

타겟이라면 True를 리턴하고, 이보다 작거나 클 경우 row , col을 위쪽 오른쪽으로 조정해 값을 찾아가면된다. 시간 복잡도는 O(M + N)이다.

### recursively

재귀적으로, D&C.

다음에 시도해볼것.