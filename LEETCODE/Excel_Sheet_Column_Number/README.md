# [LEETCODE] Excel Sheet Column Number

A -> 1, Z -> 26, AA -> 27, AB -> 28 같은 규칙일때 알파벳에 해당하는 숫자를 찾자

### 접근

26진수라고 해야할까? 헷갈릴땐 쓰면서 하는게 좋다.

이진수 101은 1*(2^2) + 0*(2^1) + 1\*(2^0)인 것처럼 문제를 해석하면 된다.

"AA"는 A가 1이기 때문에 1*(26^1) + 1*(26^0)이다.

이는 이진법에서 썼던 방법 그대로 사용해도 좋을것 같다. 더블링이라던지..