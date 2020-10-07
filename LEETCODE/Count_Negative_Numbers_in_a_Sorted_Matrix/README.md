# [LEETCODE] Count Negative Numbers in a Sorted Matrix

정렬된 2차원 배열에서 음수 갯수 세기

### 접근

- bruteforce O(N^2)
  일단 우측 하단이 제일 작은 수이기 때문에 거기서부터 시작해서 순회한다. 행을 돌때 양수가 나오면 거기서 break, 윗 행으로 이동한다.

- pointer O(M+N)
  왼쪽 하단에서 시작, 좌표를 벗어나기 전까지 수행

  1. 값이 음수라면 N - j(현재 인덱스)개를 추가하고 i - 1 해서 윗 행으로 이동
  2. 값이 양수라면 j + 1 해서 옆으로 이동

- binarySearch O(M\*logN)
  각 행에서 처음 나오는 음수를 찾는데, 이진탐색으로 찾기.
