# [LEETCODE] Add and Search Word - Data structure design

Trie에서 insert 및 와일드카드('.')가 포함된 search를 갖는 WordDictionary 구현하기

### 접근

Trie를 활용해 단어를 추가 및 검색한다.

정해진 단어를 찾는게 아니고 '.' 처럼 와일드카드 형식이 포함된 문자를 찾기 때문에 여러 노드들을 추가적으로 검색해야 하는게 문제라고 생각한다.

이부분은 BFS나 DFS를 활용해 풀 수 있을것같다.

깊이를 단어의 인덱스로 생각한다면 무리없이 풀리지 않을까 싶다.
