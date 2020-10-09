# [LEETCODE] N-Repeated Element in Size 2N Array

2N 길이의 배열 A에는 N+1개의 unique한 요소가 있고, 그 중 하나는 반드시 N번 등장한다. 이때 N번 등장하는 요소의 값을 리턴.

### 접근

전부 루프해야 하므로 시간 복잡도는 O(N). 이를 카운팅하면 O(N)의 공간 복잡도를 갖게끔 문제를 풀 수 있다.

다만 알아두면 좋을 사실은 문제에서 말한 조건을 만족하려면 N번 등장하는 요소가 있기 위해선 N번 등장하는 요소 말고는 모두 한번밖에 나오지 않게된다는 것.

예를 들어 N=3이라면 [1,2,3,3,3,3]처럼, 단 하나의 숫자만 두번 이상 등장하게 된다는 것이다.

이를 활용해 O(1)의 공간 복잡도를 갖도록 문제를 풀 수 있다.

```py
class Solution:
    def repeatedNTimes(self, A):
        for i in range(len(A)):
            if A[i - 1] == A[i] or A[i - 2] == A[i]:
                return A[i]
        return A[0]
```
