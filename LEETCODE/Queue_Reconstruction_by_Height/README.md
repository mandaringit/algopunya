# [LEETCODE] Queue Reconstruction by Height

높이에 따라 큐 정렬하기

### 접근

느낌엔 정렬 후 어떻게 풀면 될거같긴 한데 쉽게 생각이 잘 안났다.

다른 사람의 풀이를 참고했는데, 큰 키로 정렬 (동일하다면 두번째 인자로 정렬) 후 각각 k번째 인덱스에 삽입하면 된다.

시간 복잡도는 정렬에 O(NlogN), 삽입에 O(N^2)이 걸린다.

[이 풀이를 참고](https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution)했다.
