# [LEETCODE] First Bad Version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.

### 약간 다른 이진 탐색, LowerBound

이전엔 보통 타겟이 주어지고 그것을 찾아내는데 주안점을 뒀다면, 이런 문제는 한쪽에 근접해가는 모양이라고 봐도 될까? 특정 값 이상이 처음으로 나타나는 경우를 찾는것. 이 문제는 BadVersion이 처음 나타나는 경우를 찾는 것이다.

위 문제에서 좋은 버전을 g, 안좋은 버전을 b로 표기하면 대강 이런 식으로 배열이 되어 있을 것이다. `[g,g,g,b,b,b,b]`

조건을 검색할 때, 이 위치에 있는 값이 BadVersion이다 ! 해서 답이 딱 나오는게 아니라, 처음으로 BadVersion이 되는 위치를 찾아야하기 때문에

- Not Bad Version -> left를 mid + 1로 땡기고
- Bad Version -> right를 mid로 땡긴다. 이 경우 mid - 1이 아닌 이유는 이 mid 값이 정답일 수도 있으니까.

이렇게 줄여나가다 보면 left = 3, right = 3 일때 루프가 종료되며, 3이라는 인덱스가 최초로 Bad Version이 나온 경우라고 유추할 수 있다.
