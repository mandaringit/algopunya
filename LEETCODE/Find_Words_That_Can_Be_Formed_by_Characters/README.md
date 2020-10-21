# [LEETCODE] Find Words That Can Be Formed by Characters

특정 단어안에 있는 알파벳들로 구성 가능한 단어들 구하기

### 접근

먼저 가능한 알파벳을 Counter를 통해 구한다. Map 자료구조.

그리고 각 단어들도 Counter를 통해 Map으로 만든 다음 각 키 & 값을 가능한 알파벳과 비교한다.
