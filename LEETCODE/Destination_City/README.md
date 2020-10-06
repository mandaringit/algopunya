# [LEETCODE] Destination City

다른곳으로 가는 길이 없는 도시 구하기

### 접근

각 경로에서 0번째 인덱스에 있는 도시는 모두 출발지가 되므로 destination city가 될 수 없다. 그렇기 때문에 전체 도시에서 desination city가 안되는 도시를 빼면 destination city 딱 하나만 남게 된다.

N이 path의 길이, s가 모든 도시의 길이 t가 dest city가 아닌 것의 길이라 하면 시간복잡도는 O(N + s + t)
