# [LEETCODE] Split a String in Balanced Strings

L과 R이 동일한 갯수만큼 들어간 string을 balanced string이라고 할 때, 문자열 s에서 balanced string의 갯수는?

### 접근

스택과 같은 접근을 생각했었는데, L이나 R이 먼저 나올 수 있어서 그냥 갯수만 세도 괜찮겠다 싶었다. R의 갯수 == L의 갯수 일때 카운트 하면 된다.
