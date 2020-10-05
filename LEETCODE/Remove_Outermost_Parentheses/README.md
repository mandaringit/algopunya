# [LEETCODE] Remove Outermost Parentheses

유효한 괄호 문자열 S가 주어질 때, 그것의 primitive decomposition 구하기.

- 유효한 괄호 문자열 S는 비어 있지 않은 경우 "primitive" 하며 A 및 B가 비어 있지 않은 유효한 괄호 문자열을 사용하여 S = A + B로 분할하는 방법이 없는 경우이다.

- S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

- 추상화 : 결론은 가장 바깥쪽 괄호만 (모두) 벗겨내라는 말

### 접근

1. 가장 바깥쪽의 괄호 `(` 를 체크 (pair += 1)
2. 가장 바깥쪽 괄호가 있을 때 (pair >= 1)
   - `(` 가 오면 `pair += 1` 및 괄호 보관
   - `)` 가 오면 `pair -= 1`
     - 감소 후에도 여전히 `pair >= 1` 이라면 배열에 보관
     - 만약 pair가 0이 된다면 가장 바깥쪽 괄호의 쌍이 되는 `)` 라는 뜻. 이는 포함하지 않는다.
3. 마지막까지 순회 후 마지막에 보관한 괄호 join.

1, 2번 과정을 어떻게 잘 체크할지 고민해보면 더 좋은 방법도 있을것 같다.
