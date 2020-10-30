# [LEETCODE] Island Perimeter

섬의 둘레 구하기

### 접근

섬의 최대 크기는 100 \* 100이므로 O(N^2)도 무리가 없다.

모두 순회하면서 섬인것들일때 4를 더하고, 거기서 왼쪽과 위쪽을 봐서 섬이 있으면 중복된 2개를 빼준다.

DFS나 BFS를 이용한 풀이도 괜찮을 것 같다.

다만 섬의 크기가 커진다면 불필요하게 도는 시간이 많아지지 않을까?